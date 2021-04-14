%undefine _debugsource_packages

Name: sysvbanner
Summary: System-V banner clone
Version: 1.0.15
Release: 4
Group: misc
URL: https://github.com/uffejakobsen/sysvbanner
License: Public Domain
Source0: %{name}_%{version}.tar.gz

%description
Displays a `banner' text the same way as the System V banner does: horizontally.

%prep
%setup -q
sed -i -e 's|80|256|' -e 's|10|32|' banner.c

%build
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
mv %{buildroot}%{_bindir}/banner %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_mandir}/man1/banner.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc debian/changelog debian/copyright
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Jun 28 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.15
- Rebuilt for Fedora
