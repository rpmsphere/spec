Name:           nweb
Version:        23
Release:        3.1
Summary:        Tiny and safe webserver that serves static pages only
Group:          System/Servers
License:        ASL 2.0
URL:            https://www.ibm.com/developerworks/systems/library/es-nweb/
Source0:        https://public.dhe.ibm.com/systems/power/community/aix/nweb/nweb.zip#/%{name}-%{version}.zip
Patch0:         nweb-23-add-more-extensions.patch

%description
Have you ever wanted to run a tiny, safe web server without worrying about
using a fully blown web server that could be complex to install and configure?
Do you wonder how to write a program that accepts incoming messages with a
network socket? Have you ever just wanted your own Web server to experiment
and learn with?

Well, look no further -- nweb is what you need. This is a simple Web server
that has only 200 lines of C source code. It runs as a regular user and can't
run any server-side scripts or programs, so it can't open up any special
privileges or security holes. 

%prep
%setup -c
%patch0 -p1

%build
gcc %{optflags} %{name}%{version}.c -o %{name}

%install
install -d %{buildroot}%{_sbindir}
install -D -p -m 0755 %{name} %{buildroot}%{_sbindir}

%files
%doc README.txt
%doc client.c index.html nigel.jpg favicon.ico
%{_sbindir}/%{name}

%changelog
* Mon Jul 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 23
- Rebuild for Fedora
* Fri May 18 2018 kekepower <kekepower> 23-2.mga7
  (not released yet)
+ Revision: 1230398
- Update patch to include more mime types
- Use optflags instead of hard coding options
* Fri Apr 06 2018 kekepower <kekepower> 23-1.mga7
+ Revision: 1215709
- imported package nweb
