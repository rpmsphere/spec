Name:           tlinux
Version:        1.2.1
Release:        1%{?dist}
Summary:        Thin client programs in C/C++
License:        commercial, freeware
URL:            https://github.com/thintron/tlinux
Source0:        %{name}-%{version}.tar.gz
Source1:	%{name}-changelog
BuildRequires:  qt4-devel
BuildRequires:  gtk3-devel
Requires:       freerdp
Requires:       psmisc
Requires:       x11vnc
Requires:       alsa-utils
Requires:       dmidecode

%description
Various programs for Thin Client, written with Qt4/GTK3.

%prep
%setup -q
cp %{SOURCE1} ChangeLog

%build
./build.sh

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 tlinux_ver %{buildroot}%{_sysconfdir}/%{name}_ver
install -Dm755 tlinux.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_bindir}/TLinux
for i in Display Information LoginForm Network Ping Preference RDP Serial Shutdown Traceroute VNCserver Volume ; do
  install $i/$i %{buildroot}%{_bindir}/TLinux
done
install -m644 */*.qm %{buildroot}%{_bindir}/TLinux
install -m644 VNCserver/VNCserver_* Preference/SystemLanguage %{buildroot}%{_bindir}/TLinux

%files
%doc ChangeLog
%{_bindir}/%{name}
%{_bindir}/TLinux
%{_sysconfdir}/%{name}_ver

%changelog
* Tue Jun 16 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.1
- Initial package
