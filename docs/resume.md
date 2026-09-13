---
layout: page
title: Experience & education
menutitle: Resume
menuorder: 3
share: false
excerpt: Experience in Zero Trust networking, systems engineering, compilers, and security research.
---

[Download resume (PDF)]({{ '/assets/Abdul-Manan-Resume.pdf' | relative_url }}) · [LinkedIn](https://www.linkedin.com/in/fnu-abdul-manan)

## Experience

### Cloudflare
**Systems Engineer** · Austin, TX · Nov 2025 - Present

- Contribute to [Cloudflare One](https://developers.cloudflare.com/cloudflare-one/) and its Zero Trust data plane, supporting policy-driven traffic routing across a global edge network of 50,000+ servers handling billions of requests daily.
- Build and enhance networking components for TCP termination, regionalization, and security policy enforcement.
- Improve traffic-flow debugging through packet sampling and telemetry for routing decisions, performance, and policy enforcement.

### InterSystems Corporation
**Developer Support Engineer** · Cambridge, MA · Jul 2023 - Nov 2025

- Diagnosed networking and kernel security issues in mission-critical InterSystems applications.
- Developed an ObjectScript performance-tracing API capturing CPU cycles, network connections, database accesses, and function calls.
- Modified the C ObjectScript compiler to insert instrumentation hooks during compilation.

### Siemens
**Software Development Intern** · Princeton, NJ · Jun 2022 - Aug 2022

- Designed and prototyped a [Zero Trust security extension for 5G core services](https://doi.org/10.1109/AICCSA56895.2022.10017774) using Free5GC, Go, and C++.
- Supported 100,000+ devices with less than 1% performance overhead in the prototype.

### Brown University
**Research Assistant** · Providence, RI · Jan 2021 - May 2023

- Built a Node.js syscall-filtering tool using dynamic program analysis, reducing exploit potential by 95% with 0-2% performance overhead.
- Developed distributed QUIC fuzz testing that discovered bugs in Meta and Cloudflare implementations.
- Compared QUIC and TCP performance: QUIC was up to 20% faster for smaller objects, with negligible differences for pages of 1 MB or larger.

### Lahore University of Management Sciences
**Research Assistant** · Lahore, Pakistan · Jan 2019 - May 2020

- Investigated mobile video bottlenecks: memory pressure reduced frame rates by up to 80%; kernel memory management and disk I/O caused frame drops of up to 40%.

Coauthored paper: [Mobile Web Browsing Under Memory Pressure](https://cs.brown.edu/people/tab/papers/CCR20.pdf). Related video research: [Coal Not Diamonds: How Memory Pressure Falters Mobile Video QoE](https://talha.cs.illinois.edu/files/coal-not-diamonds.pdf), by Talha Waheed and colleagues (I am not a coauthor).

## Education

**Brown University** · Sc.M. in Computer Science · May 2023<br>
GPA: 4.0/4.0. Graduate study in distributed systems, compilers and program analysis, machine learning, cryptography, and software security.

**Lahore University of Management Sciences** · BS in Computer Science · May 2020<br>
Graduated with Distinction. Focus: computer networking and security.

## Selected project: tinyOS-rs

Built a 32-bit RISC-V operating system in `no_std` Rust with Sv32 virtual memory, process scheduling, system calls, VirtIO drivers, a tar filesystem, a shell, and a TCP/IP stack. Runs in QEMU.

## Technical skills

**Languages:** C, C++, Rust, Python, Go, JavaScript<br>
**Systems & tools:** Linux, Bash, Docker, eBPF, LLVM, x86, microservices, MySQL<br>
**Areas:** TCP/IP, QUIC, Zero Trust, distributed systems, compiler instrumentation, program analysis, fuzz testing

## Publications

- [*Extending 5G services with Zero Trust security pillars: a modular approach.*](https://doi.org/10.1109/AICCSA56895.2022.10017774) IEEE/ACS AICCSA, 2022.
- [*Mobile web browsing under memory pressure.*](https://cs.brown.edu/people/tab/papers/CCR20.pdf) ACM SIGCOMM Computer Communication Review, 2020.
