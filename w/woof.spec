Name:		woof
Version:	20220202
Release:	1
Summary:	Simple Web-based File Exchange
Source0:	https://github.com/simon-budig/woof/archive/refs/heads/master.zip#/%{name}-master.zip
URL:		http://www.home.unix-ag.org/simon/woof.html
Group:		Networking/Remote access
License:	GPLv3+
BuildArch:	noarch
Requires:	python tar net-tools

%description
Woof (Web Offer One File) tries a different approach. It assumes that
everybody has a web-browser or a commandline web-client installed. Woof is a
small simple stupid webserver that can easily be invoked on a single
file. Your partner can access the file with tools he trusts (e.g. wget). No
need to enter passwords on keyboards where you don't know about keyboard
sniffers, no need to start a huge lot of infrastructure.

%prep
%setup -q -n %{name}-master

%build

%install
install -D -m0755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 20220202
- Rebuilt for Fedora
* Mon Feb 08 2016 umeabot <umeabot> 20120531-7.mga6
+ Revision: 946479
- Mageia 6 Mass Rebuild
* Wed Oct 15 2014 umeabot <umeabot> 20120531-6.mga5
+ Revision: 746001
- Second Mageia 5 Mass Rebuild
* Tue Sep 16 2014 umeabot <umeabot> 20120531-5.mga5
+ Revision: 690362
- Mageia 5 Mass Rebuild
* Fri Oct 18 2013 umeabot <umeabot> 20120531-4.mga4
+ Revision: 520175
- Mageia 4 Mass Rebuild
* Mon Jan 14 2013 umeabot <umeabot> 20120531-3.mga3
+ Revision: 385830
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Dec 18 2012 dams <dams> 20120531-2.mga3
+ Revision: 332621
- clean specfile
- fix version
* Tue Dec 18 2012 kharec <kharec> 0.20120531-1.mga3
+ Revision: 332615
- imported package woof
