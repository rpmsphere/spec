Name: firefox
Summary: Mozilla Firefox Web browser
Version: 11.0
Release: 1%{?dist}.bin
License: MPLv1.1 or GPLv2+ or LGPLv2+
Group: Applications/Internet
Source0: http://ftp.yz.yamagata-u.ac.jp/pub/network/mozilla//firefox/releases/11.0/linux-i686/zh-TW/%{name}-%{version}.tar.bz2
Source1: %{name}.png
Source2: mozilla-%{name}.desktop
URL: http://www.mozilla.org/projects/firefox/
BuildRoot: %{_tmppath}/build-%{name}-%{version}
ExclusiveArch: %{ix86}

%description
Mozilla Firefox is an open-source web browser, designed for standards
compliance, performance and portability.

%prep
%setup -q -n %{name}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/%{name}-11
cp -a * %{buildroot}%{_libdir}/%{name}-11
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/mozilla-%{name}.desktop
install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_libdir}/%{name}-11
./%{name}
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/mozilla-%{name}.desktop
%{_libdir}/%{name}-11

%changelog
* Wed Mar 14 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 11.0
- Rebuild for OSSII
