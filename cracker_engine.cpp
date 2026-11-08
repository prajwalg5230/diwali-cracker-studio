// cracker_engine.cpp - High-Performance C++ WebAssembly Physics Engine
// Compiled with clang --target=wasm32 -nostdlib -Wl,--no-entry -Wl,--export-all -O3

#define WASM_EXPORT __attribute__((visibility("default"))) extern "C"

#define MAX_PARTICLES 4000

struct Particle {
    float x, y, z;
    float vx, vy, vz;
    float r, g, b;
    float size;
    float gravity;
    float decay;
    float friction;
    float bounce;
    float life;
    int active;
};

// Global memory buffer for particles (Direct linear memory for zero-copy JS access)
static Particle particles[MAX_PARTICLES];
static int active_count = 0;

static unsigned int g_seed = 123456789;

WASM_EXPORT void seed_random(unsigned int s) {
    g_seed = s;
}

static float fast_sin(float x) {
    // Normalize to -PI .. PI
    const float PI = 3.14159265f;
    const float TWO_PI = 6.2831853f;
    while (x > PI) x -= TWO_PI;
    while (x < -PI) x += TWO_PI;
    // High-accuracy Taylor polynomial for sin(x)
    float x2 = x * x;
    return x * (1.0f - x2 * (1.0f / 6.0f - x2 * (1.0f / 120.0f - x2 / 5040.0f)));
}

static float fast_cos(float x) {
    return fast_sin(x + 1.5707963f);
}

WASM_EXPORT int get_max_particles() {
    return MAX_PARTICLES;
}

WASM_EXPORT Particle* get_particles_buffer() {
    return particles;
}

WASM_EXPORT int get_particle_size_bytes() {
    return sizeof(Particle);
}

WASM_EXPORT void clear_particles() {
    for (int i = 0; i < MAX_PARTICLES; i++) {
        particles[i].active = 0;
        particles[i].life = 0.0f;
    }
    active_count = 0;
}

WASM_EXPORT int spawn_particle(
    float x, float y, float z,
    float vx, float vy, float vz,
    float r, float g, float b,
    float size, float gravity, float decay, float friction, float bounce
) {
    for (int i = 0; i < MAX_PARTICLES; i++) {
        if (!particles[i].active || particles[i].life <= 0.0f) {
            particles[i].x = x;
            particles[i].y = y;
            particles[i].z = z;
            particles[i].vx = vx;
            particles[i].vy = vy;
            particles[i].vz = vz;
            particles[i].r = r;
            particles[i].g = g;
            particles[i].b = b;
            particles[i].size = size;
            particles[i].gravity = gravity;
            particles[i].decay = decay;
            particles[i].friction = friction;
            particles[i].bounce = bounce;
            particles[i].life = 1.0f;
            particles[i].active = 1;
            return i;
        }
    }
    return -1;
}

// C++ Physics step: updates all active particles with gravity, air drag, and floor collision
WASM_EXPORT int step_physics(float dt) {
    int live = 0;
    for (int i = 0; i < MAX_PARTICLES; i++) {
        if (!particles[i].active) continue;

        particles[i].x += particles[i].vx;
        particles[i].y += particles[i].vy;
        particles[i].z += particles[i].vz;

        // Air drag / friction
        particles[i].vx *= particles[i].friction;
        particles[i].vz *= particles[i].friction;

        // Gravity
        particles[i].vy -= particles[i].gravity;

        // Ground floor collision
        if (particles[i].y <= 0.04f) {
            particles[i].y = 0.04f;
            if (particles[i].bounce > 0.01f) {
                particles[i].vy = -particles[i].vy * particles[i].bounce;
                particles[i].vx *= 0.78f;
                particles[i].vz *= 0.78f;
            } else {
                particles[i].vy = 0.0f;
                particles[i].vx *= 0.92f;
                particles[i].vz *= 0.92f;
            }
        }

        particles[i].life -= particles[i].decay;
        if (particles[i].life <= 0.0f) {
            particles[i].active = 0;
        } else {
            live++;
        }
    }
    active_count = live;
    return live;
}

// Procedural unique snake generator (returns 3D position at segment step t)
// Calculates unique non-repeating curves based on dynamic seed
WASM_EXPORT float get_snake_x(float t, float seed) {
    float angle1 = t * 0.45f + seed;
    float angle2 = t * 1.15f + seed * 2.1f;
    return (0.35f * fast_sin(angle1) + 0.18f * fast_cos(angle2));
}

WASM_EXPORT float get_snake_z(float t, float seed) {
    float angle1 = t * 0.52f + seed * 1.4f;
    float angle2 = t * 1.35f + seed * 0.7f;
    return (0.35f * fast_cos(angle1) + 0.18f * fast_sin(angle2));
}

WASM_EXPORT float get_snake_y(float t, float seed) {
    return 0.15f + t * 0.055f;
}
