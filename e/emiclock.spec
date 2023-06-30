%undefine _debugsource_packages

Summary: An X Window System analog clock
Name: emiclock
Version: 2.0.2
Release: 10.1
License: distributable
Group: Amusements/Games
Source0: emiclock-2.0.2.tar.gz
Patch0: emiclock-2.0.2.jg.patch
BuildRequires: imake, libXt-devel, libXext-devel, libXaw-devel
URL: https://www003.upp.so-net.ne.jp/motosoft/

%description
EmiClock is an analog clock for X.  EmiClock displays a Japanese girl
on the clock face whose costume will change automatically every hour.
EmiClock can be used for an alarm clock and/or to sound chimes at set
times.

%prep
%setup -q
%patch0 -p1

%build
xmkmf
make depend
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 emiclock $RPM_BUILD_ROOT%{_bindir}/emiclock
install -Dm644 resources/Xaw/EmiClock.ad $RPM_BUILD_ROOT%{_datadir}/X11/app-defaults/EmiClock
install -Dm644 resources/R6/EUC/EmiClock.ad $RPM_BUILD_ROOT%{_datadir}/X11/ja_JP.ujis/app-defaults/EmiClock
install -Dm644 sounds/myu.au $RPM_BUILD_ROOT%{_prefix}/lib/EmiClock/myu.au
install -Dm644 emiclock._man $RPM_BUILD_ROOT%{_mandir}/man1/emiclock.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc 00.README COPYRIGHT COPYRIGHT.en ChangeLog INSTALL.ja MANIFEST README.ja doc/README-OS.ja doc/TECH-NOTE.ja doc/Original/README.mac.ja doc/Original/README.win.ja 
%{_bindir}/emiclock
%{_datadir}/X11/app-defaults/EmiClock
%{_prefix}/lib/EmiClock/myu.au
%{_datadir}/X11/ja_JP.ujis/app-defaults/EmiClock
%{_mandir}/man1/emiclock.1.gz

%changelog
* Fri Mar 04 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.2
- Rebuilt for Fedora
* Fri Apr 21 2000 Hironobu ABE <hiro-a@mars.dti.ne.jp>
- 1st release
