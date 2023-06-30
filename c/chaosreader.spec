Name:          chaosreader
Version:       0.94
Release:       4.1
Summary:       An open source tool to trace TCP/UDP/... sessions and fetch application data
Group:         Network/Monitoring
URL:           https://www.brendangregg.com/chaosreader.html
Source:        https://downloads.sourceforge.net/chaosreader/chaosreader%{version}
License:       GPL
BuildArch:     noarch

%description
Chaosreader is an open source tool to trace TCP/UDP/... sessions and fetch application data from snoop or tcpdump logs.
This is a type of "any-snarf" program, as it will fetch telnet sessions, FTP files, HTTP transfers (HTML, GIF, JPEG, ...), SMTP emails, ... from the captured data inside network traffic logs.
A html index file is created that links to all the session details, including realtime replay programs for telnet, rlogin, IRC, X11 or VNC sessions; and reports such as image reports and HTTP GET/POST content reports.
Chaosreader can also run in standalone mode - where it invokes tcpdump or snoop (if they are available) to create the log files and then processes them.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 %{SOURCE0} \
   $RPM_BUILD_ROOT%{_bindir}/%{name}

#$RPM_BUILD_ROOT%{_bindir}/%{name} --help2 > README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
#doc README

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.94
- Rebuilt for Fedora

* Wed Aug 29 2007 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.94-1mamba
- package created by autospec
