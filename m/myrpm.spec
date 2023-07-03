Summary: 		Tool suite for quick RPM build 
Name:			myrpm
Version: 		5.38
Release:	   	2	
License: 		GPL
URL: 			https://www.jmrenouard.fr/
Source0: 		%{name}-%{version}.tar.gz
Group: 			System/Administration
BuildArch:		noarch
Requires: perl
Requires: perl-Text-Template
Requires: perl-Archive-Tar

%description 
Tools allowing you to build RPMs quickly with group,user, symbolic links and
permissions embedded. This tool suite manages files nature.

%prep
%setup -c -q

%build

%install
rm -Rf %{buildroot}
%{__install} -d %{buildroot}%{_bindir}
%{__install} -m 0755 "usr/local/myrpm/build_tpl.sh" "%{buildroot}/usr/bin/build_tpl.sh"
%{__install} -m 0755 "usr/bin/xmyrpm" "%{buildroot}/usr/bin/xmyrpm"
%{__install} -m 0755 "usr/bin/pushRpm" "%{buildroot}/usr/bin/pushRpm"
%{__install} -m 0755 "usr/bin/myrpm" "%{buildroot}/usr/bin/myrpm"
%{__install} -m 0755 "usr/bin/rpmMacrosConfig" "%{buildroot}/usr/bin/rpmMacrosConfig"
%{__install} -m 0755 "usr/bin/rpmFactory" "%{buildroot}/usr/bin/rpmFactory"

%clean
rm -Rf %{buildroot}

%files
%doc usr/share/doc/myrpm-*/README
%{_bindir}/*

%changelog
* Sun Sep 18 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.38
- Rebuilt for Fedora
* Tue Mar 04 2014 Jean-Marie Renouard<jmrenouard@gmail.com> myrpm-5.38-2
- MyRPM 5.38-2
- Generated version.
