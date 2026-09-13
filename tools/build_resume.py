from pathlib import Path
from xml.sax.saxutils import escape
import json, shutil
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
base=Path(__file__).resolve().parent.parent
roles=json.loads((base/'tools/resume_data.json').read_text())
out=base/'output/pdf/Abdul-Manan-Resume.pdf'
styles={
'name':ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=25,leading=29,textColor=HexColor('#163d47'),spaceAfter=5),
'tag':ParagraphStyle('tag',fontName='Helvetica',fontSize=11,leading=15,textColor=HexColor('#176b75'),spaceAfter=6),
'body':ParagraphStyle('body',fontName='Helvetica',fontSize=9.6,leading=13.4,spaceAfter=5),
'contact':ParagraphStyle('contact',fontName='Helvetica',fontSize=9,leading=13,spaceAfter=10),
'section':ParagraphStyle('section',fontName='Helvetica-Bold',fontSize=11,leading=15,textColor=HexColor('#176b75'),spaceBefore=12,spaceAfter=7),
'role':ParagraphStyle('role',fontName='Helvetica-Bold',fontSize=10.5,leading=14,spaceAfter=2),
'meta':ParagraphStyle('meta',fontName='Helvetica',fontSize=9,leading=12,textColor=HexColor('#596269'),spaceAfter=5),
'bullet':ParagraphStyle('bullet',fontName='Helvetica',fontSize=9.6,leading=13.4,leftIndent=10,firstLineIndent=-8,spaceAfter=4)}
story=[]
def p(text,style='body'): return Paragraph(text,styles[style])
def section(text): story.append(p(text.upper(),'section'))
def role(r):
 company,title,loc,dates,bullets=r
 story.append(KeepTogether([p(escape(company)+' | '+escape(title),'role'),p(escape(loc)+' · '+escape(dates),'meta'),p('- '+escape(bullets[0]),'bullet')]))
 story.extend(p('- '+escape(b),'bullet') for b in bullets[1:]);story.append(Spacer(1,6))
story += [p('ABDUL MANAN','name'),p('SYSTEMS ENGINEERING / NETWORKING / SECURITY','tag'),p('Austin, TX · (718) 578-3399 · <link href="mailto:fnu.abdul.manan@gmail.com">fnu.abdul.manan@gmail.com</link><br/><link href="https://www.linkedin.com/in/fnu-abdul-manan">linkedin.com/in/fnu-abdul-manan</link> · <link href="https://abdul-manaan.github.io">abdul-manaan.github.io</link>','contact'),p('Systems engineer working on Cloudflare\'s Zero Trust data plane. Experience in network infrastructure, compiler instrumentation, security research, and performance analysis. Strong background in C/C++, Python, Go, and Linux systems.')]
section('Experience')
for r in roles[:3]: role(r)
section('Technical skills')
story += [p('<b>Languages:</b> C, C++, Python, Go, JavaScript'),p('<b>Systems &amp; tools:</b> Linux, Bash, Docker, eBPF, LLVM, x86, microservices, MySQL'),p('<b>Areas:</b> TCP/IP, QUIC, Zero Trust, distributed systems, program analysis, fuzz testing')]
story.append(PageBreak())
section('Research experience')
for r in roles[3:]: role(r)
section('Selected projects')
for title,desc in [('Static taint analysis','Implemented an LLVM pass in C++ to identify information leakage in Rust applications.'),('Kernel-level network monitoring','Built an eBPF tool for Ethernet, IP, and TCP packet inspection and service-level CPU utilization.'),('Protocol implementation','Implemented QUIC alongside UDP and Ethernet stack components in C.')]:
 story.append(p('<b>'+title+'.</b> '+desc))
section('Education')
story += [p('Brown University | Sc.M. in Computer Science','role'),p('Providence, RI · May 2023 · GPA: 4.0/4.0','meta'),p('Coursework: distributed systems, compilers and program analysis, machine learning, applied cryptography, software security and exploitation.'),Spacer(1,5),p('Lahore University of Management Sciences | BS in Computer Science','role'),p('Lahore, Pakistan · May 2020 · Graduated with Distinction','meta'),p('Focus: computer networking and security.')]
section('Publications')
story += [p('<b>Extending 5G services with Zero Trust security pillars: a modular approach.</b><br/>IEEE/ACS 19th International Conference on Computer Systems and Applications, 2022.'),p('<b>Mobile web browsing under memory pressure.</b><br/>ACM SIGCOMM Computer Communication Review, 2020.')]
def footer(c,d):
 c.setStrokeColor(HexColor('#d7e2e4'));c.line(44,37,568,37)
 c.setFont('Helvetica',8);c.setFillColor(HexColor('#596269'));c.drawString(44,25,'Abdul Manan | Systems & Networking');c.drawRightString(568,25,str(d.page))
SimpleDocTemplate(str(out),pagesize=(612,792),leftMargin=44,rightMargin=44,topMargin=36,bottomMargin=48,title='Abdul Manan - Resume',author='Abdul Manan').build(story,onFirstPage=footer,onLaterPages=footer)
shutil.copyfile(out,base/'assets/Abdul-Manan-Resume.pdf')
print(out)
