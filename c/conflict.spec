Name:           conflict
Version:        6.14
Release:        20100629.1
License:        MIT
Summary:        List Filename Conflicts
URL:            http://invisible-island.net/conflict/
Group:          Productivity/File utilities
Source0:        ftp://invisible-island.net/%{name}/%{name}-20100627.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CONFLICT examines the user-specifiable list of programs, looking for instances
in the user's path which conflict (i.e., the name appears in more than one
point in the path).

%prep
%setup -q -n %{name}-20100627

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc CHANGES COPYING README
%{_bindir}/conflict
%{_mandir}/man1/conflict.1.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 6.14
- Rebuilt for Fedora
* Sun Aug 26 2012 asterios.dramis@gmail.com
- Updated source url and source package (use the versioned one that is provided
  in the package homepage).
- Changed License to MIT.
- Removed %%clean section (not needed anymore).
* Sun Feb 20 2011 asterios.dramis@gmail.com
- Minor fixes in %%files section.
* Sun Feb 20 2011 asterios.dramis@gmail.com
- Corrected the package name in the spec file header.
* Sun Feb 20 2011 asterios.dramis@gmail.com
- Spec file updates:
  * Minor fixes in spec file.
  * Changed License: to BSD-style.
  * Minor fixes in %%files section.
* Fri Dec 10 2010 asterios.dramis@gmail.com
- Spec file updates after spec-cleaner run.
* Fri Nov 12 2010 asterios.dramis@gmail.com
- Corrected the release number in the spec file.
* Wed Nov 10 2010 asterios.dramis@gmail.com
- Spec file updates after spec-cleaner run.
* Wed Nov 10 2010 asterios.dramis@gmail.com
- Corrected the release number in the spec file.
* Tue Nov  9 2010 asterios.dramis@gmail.com
- Cosmetic improvements in spec file.
* Sun Nov  7 2010 asterios.dramis@gmail.com
- Initial release (version 20100627).
