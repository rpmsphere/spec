%global __os_install_post %{nil}
%undefine _debugsource_packages

Summary: Classic Rexx Implementation
Name: brexx
Version: 2.1.9
Release: 1
License: GPLv2
Group: Development/Languages
URL: https://github.com/vlachoudis/brexx
Source: brexx-master.zip
BuildRequires: readline-devel
BuildRequires: libnsl2-devel

%description
REXX is a programming language designed by Michael Cowlishaw of
IBM UK Laboratories.  In his own words:  "REXX is a procedural
language that allows programs and algorithms to be written in a
clear and structured way."
 
%prep
%setup -q -n %{name}-master
sed -i 's|lib/$|%{_lib}/|' make.cnf

%build
make linux

%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=%{buildroot}/usr
install AUTHORS ChangeLog COPYING README %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_bindir}/rexx %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}/etc/profile.d
echo export RXLIB=/usr/lib/brexx > %{buildroot}%{_sysconfdir}/profile.d/brexx.sh
echo setenv RXLIB /usr/lib/brexx > %{buildroot}%{_sysconfdir}/profile.d/brexx.csh

sed -i 's|local/bin/rexx|bin/brexx|' %{buildroot}%{_datadir}/%{name}/*.r

%files
%{_docdir}/%{name}
%{_datadir}/%{name}
%{_libdir}/lib*
/usr/lib/%{name}
%{_includedir}/%{name}
%{_bindir}/%{name}
%{_sysconfdir}/profile.d/brexx.*

%changelog
* Tue Oct 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.9
- Rebuilt for Fedora
