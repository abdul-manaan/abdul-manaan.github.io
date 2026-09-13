---
layout: post
title: What is AMP?
excerpt: "What is Google AMP and why it is important?"
modified: 8/12/2020, 18:40:00
tags: [amp, google, webpage, optimizations]
comments: true
category: blog
---

<img src="../../images/amp-logo.png" alt="Google AMP Logo">

AMP is an alternative framework to HTML with some restrictions to ensure reliable page performance. It simplifies the original webpage by stripping away “unnecessary” code and by replacing some of the standard html tags with its own tags (like replacing `<img>` tag with `<amp-img>` tag). AMP does a lot of other optimizations that helps in reducing the page load time and size. We can categorize these optimizations into following 3 categories:

## Page Simplification
Traditional web pages download a lot of third-party resources that include different scripts, stylesheets and fonts etc. However, the amp pages are much more simpler. It does not allow external stylesheets, all the CSS must be inlined and has a size limit of 50 kilobytes. Similarly, it only allows javascripts in the iframes or in special `<amp-script>` tags and must be asynchronous. This makes sure that the javascript is not blocking the rendering of main page. To avoid expensive style re-calculations, external resources such as images, ads or iframes must state their size in the HTML so that AMP can determine each element’s size and position before resources are downloaded. AMP  provides an extensive library of ready-to-go components and many of them are interactive elements and they do not require any supporting javascript code. For example, figure (\ref{f:amp-example}) shows an example of how functionality of a button can be implemented in traditional web and in AMP.

## Page Load Performance Optimizations
To optimize the page loading, AMP makes use of preconnect API that initiates an early connection with servers (which will be used later to fetch resources), which includes the DNS lookup, TCP handshake, and optional TLS negotiation. Pre-rendering is also done to further reduce the loading time of AMP pages; pre-rendering is rendering the amp page before the user actually navigates to that page. During pre-rendering, AMP downloads and renders resources that are above-the fold, but it does not render CPU intensive things. Similarly, when AMP downloads resources, it optimizes downloads so that the currently most important resources are downloaded first. Images and ads are only downloaded if they are likely to be seen by the user, above the fold, or if the user is likely to quickly scroll to them. It also prefetches lazy-loaded resources (lazy loading is an optimization to defer the resource loading until the user scrolls down to that resource)

## Network Optimizations
AMP pages are also cached at Google’s AMP Cache. An AMP Cache is a proxy-based content delivery network (CDN) for delivering valid AMP documents. AMP Cache caches main html and other resources including images and fonts. It also performs several optimizations and modification on the cached page including removal of data that is invisible or difficult to see, such as certain metadata, conversion of images to smaller and mobile-friendlier image formats, such as converting GIF, PNG, and JPEG format images to WebP in browsers that support WebP, transformation of the image to a lower quality if the request includes the Save-Data header and generation of alternatively sized images to support delivery of responsively sized images. 