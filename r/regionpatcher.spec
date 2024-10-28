Name:           regionpatcher
Version:        0.4
Release:        3.1
Summary:        A simple utility to patch the region codes of dvd movies
License:        GPL-2.0
Group:          Development/Tools/Other
URL:            https://regionpatcher.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Makefile_fix.patch asterios.dramis@gmail.com -- Make the package use CFLAGS from spec file, don't strip binaries
Patch0:         Makefile_fix.patch

%description
RegionPatcher is a simple utility to patch the region codes of dvd movies.

%prep
%setup -q
%patch 0

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dpm 0755 regionpatcher %{buildroot}%{_bindir}/regionpatcher

%files
%doc COPYING README
%{_bindir}/regionpatcher

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Mon Aug 27 2012 asterios.dramis@gmail.com
- Spec file cleanup.
* Sun Sep  4 2011 asterios.dramis@gmail.com
- Initial release (version 0.4).
- Added a patch (Makefile_fix.patch) to make the package use CFLAGS from spec
  file and also don't strip binaries.
