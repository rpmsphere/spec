%undefine _debugsource_packages

Name: bsdar
Summary: BSD ar
Version: 1.0.2
Release: 7.1
Group: Applications
License: BSD
URL: https://www.freebsd.org/
Source0: https://sourceforge.net/projects/debreate/files/other/%{name}_%{version}_src.tar.gz
BuildRequires: libbsd-devel
BuildRequires: libarchive-devel
BuildRequires: elfutils-libelf-devel

%description
BSD variant of ar (The Unix Archiver) ported to Linux.

%prep
%setup -q -n %{name}
sed -i 's|archive_version|archive_version_string|' ar.c

%build
make %{?_smp_mflags}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
