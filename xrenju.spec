Summary: Simple and addictive ancient Asia's game
Name: xrenju
Version: 0.4
Release: 5.1
License: distributable
Group: Amusements/Games
Source0: xrenju_0.4-1.tar.gz
Source1: xrenju.png
BuildRequires: imake, libXpm-devel, libXt-devel, libXaw-devel, libXmu-devel, libICE-devel, libXext-devel

%description
Renju is played between two opponents on a board. The winner of the game is
the player who will be first to attain five in a row. 

%prep
%setup -q

%build
xmkmf -a
make

%install
install -D -m 0755  xrenju $RPM_BUILD_ROOT%{_bindir}/xrenju
install -D -m 0755  think_sample $RPM_BUILD_ROOT%{_bindir}/think_sample
#install -D -m 0644 XRenju.ad $RPM_BUILD_ROOT%{_datadir}/X11/ja_JP.eucJP/app-defaults/XRenju
#install -D -m 0644 debian/XRenju_zh_CN.ad $RPM_BUILD_ROOT%{_datadir}/X11/zh_CN.GB2312/app-defaults/XRenju
echo Icon=%{name} >> debian/xrenju.desktop
install -D -m 0644 debian/xrenju.desktop $RPM_BUILD_ROOT%{_datadir}/applications/xrenju.desktop
install -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/xrenju.png

%files
%doc CHANGES README README.www
%{_bindir}/xrenju
%{_bindir}/think_sample
#/usr/share/X11/ja_JP.eucJP/app-defaults/XRenju
#/usr/share/X11/zh_CN.GB2312/app-defaults/XRenju
%{_datadir}/applications/xrenju.desktop
%{_datadir}/pixmaps/xrenju.png

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Wed Apr 26 2000 Hironobu ABE <hiro-a@mars.dti.ne.jp>
- 1st release for Vine Linux 2.0
