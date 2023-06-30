%global _name GtkSysinfo

Name: gtksysinfo
Summary: System Monitoring
Version: 1.9
Release: 1
Group: Monitoring
License: GPL
URL: https://gtksysinfo.sourceforge.net/
Source0: https://master.dl.sourceforge.net/project/gtksysinfo/gtksysinfo%20Stable/%{_name}_%{version}/%{_name}%{version}.tar.gz
BuildArch: noarch

%description
GtkSysinfo is a perl-Gtk2 software for Linux which makes it possible to obtain a
maximum of informations about the system such as temperature(with lm_sensors),
CPU frequency, hardware(with PciUtils) , network , ACPI and orther.

%prep
%setup -q -n %{_name}%{version}

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_datadir}/%{name}
cp -a Sysinfo.pl Functions.pm images lang %{buildroot}%{_datadir}/%{name}
#install -Dm644 Functions.pm %{buildroot}%{_libdir}/perl5/vendor_perl/Functions.pm
cat > %{name} <<EOF
#!/usr/bin/bash
%{_datadir}/%{name}/Sysinfo.pl
EOF
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc copying README_*
%{_bindir}/%{name}
#{_libdir}/perl5/vendor_perl/Functions.pm
%{_datadir}/%{name}

%changelog
* Fri May 21 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9  
- Rebuilt for Fedora
* Sat Apr 22 2006 Pissens Sabastien <Webmaster@linboost.org> 1.9-1mdk
- First Mandriva Linux release
