---
layout: page
title: Systems, networks, and the details that make them work.
excerpt: Abdul Manan is a Systems Engineer at Cloudflare working on Zero Trust networking, distributed systems, and observability.
menutitle: Home
menuorder: 1
share: false
tags: [Abdul Manan, Cloudflare, Networking, Distributed Systems, Zero Trust]
---

I'm **Abdul Manan**, a **Systems Engineer at Cloudflare**, based in Austin, Texas. I work on **[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)**, specifically its Zero Trust data plane: the systems that proxy traffic, apply security policies, and route connections across a global edge network.

My work spans TCP termination, regionalization, and traffic observability. I enjoy understanding how systems behave under real workloads, then building the tools and infrastructure to make them faster, safer, and easier to debug.

[Download my resume (PDF)]({{ '/assets/Abdul-Manan-Resume.pdf' | relative_url }}) · [LinkedIn](https://www.linkedin.com/in/fnu-abdul-manan) · [GitHub](https://github.com/abdul-manaan) · [Email](mailto:fnu.abdul.manan@gmail.com)

## What I work on

**Networking at the edge.** Policy-driven routing, TCP termination, and reliable traffic flow across Cloudflare's Zero Trust connectivity stack.

**Observability close to the system.** Packet sampling, telemetry, compiler instrumentation, and tools that explain where time and resources go.

**Security through systems research.** Dynamic syscall filtering, QUIC fuzzing, Zero Trust extensions for 5G, and static program analysis.

## Previously

At **InterSystems**, I diagnosed networking and kernel security issues and built performance-tracing capabilities for ObjectScript applications. At **Siemens**, I prototyped a modular Zero Trust extension for 5G core services.

My research at **Brown University** explored syscall filtering, QUIC implementations, and web performance. At **LUMS**, I studied the impact of memory pressure and device bottlenecks on mobile web and video performance.

## Selected projects

- **tinyOS-rs:** A 32-bit RISC-V operating system in `no_std` Rust, with Sv32 virtual memory, process scheduling, system calls, VirtIO drivers, a tar filesystem, a shell, and a TCP/IP stack. Runs in QEMU.

- **QUIC fuzzing:** A distributed framework for analyzing production HTTP/3 implementations, uncovering bugs in Meta and Cloudflare implementations.
- **Kernel-level network monitoring:** An eBPF tool for packet inspection and service-level CPU utilization.
- **Static taint analysis:** An LLVM pass for identifying information leakage in Rust applications.
- **Protocol implementation:** QUIC, UDP, and Ethernet implementation work in C.

[Explore my experience]({{ '/resume/' | relative_url }}) · [Read my publications]({{ '/publications/' | relative_url }})
