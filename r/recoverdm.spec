Name:           recoverdm
Version:        0.20
Release:        10.1
Summary:        Recover files/disks with damaged sectors
License:        GPL-2.0
Group:          Productivity/File utilities
URL:            http://www.vanheusden.com/recoverdm/
Source0:        http://www.vanheusden.com/recoverdm/%{name}-%{version}.tgz
Source1:        http://www.vanheusden.com/license.txt
# PATCH-FIX-OPENSUSE fix_cflags.patch asterios.dramis@gmail.com -- Make the package use CFLAGS from spec file
Patch0:         fix_cflags.patch
# PATCH-FIX-OPENSUSE fix_gcc_warnings.patch asterios.dramis@gmail.com -- Fix some gcc compilation warnings that make rpm post-build-checks fail
Patch1:         fix_gcc_warnings.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program will help you recover disks with bad sectors. You can recover
files as well complete devices.

In case if finds sectors which simply cannot be recoverd, it writes an empty
sector to the outputfile and continues. If you're recovering a CD or a DVD and
the program cannot read the sector in "normal mode", then the program will try
to read the sector in "RAW mode" (without error-checking etc.).

This toolkit also has a utility called 'mergebad': mergebad merges multiple
images into one. This can be useful when you have, for example, multiple CD's
with the same data which are all damaged. In such case, you can then first use
recoverdm to retrieve the data from the damaged CD's into image-files and then
combine them into one image with mergebad.

%prep
%setup -q
%patch0
%patch1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
install -Dpm 0755 mergebad %{buildroot}%{_bindir}/mergebad
install -Dpm 0755 recoverdm %{buildroot}%{_bindir}/recoverdm
cp -af %{SOURCE1} .

%files
%defattr(-,root,root)
%doc license.txt readme.txt
%{_bindir}/mergebad
%{_bindir}/recoverdm

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20
- Rebuilt for Fedora
* Mon Aug 27 2012 asterios.dramis@gmail.com
- Spec file cleanup.
- Updated License to GPL-2.0 (SPDX style).
* Sun Feb 20 2011 asterios.dramis@gmail.com
- Spec file updates:
  * Minor fixes in spec file.
  * Added description for the patches based on openSUSE Patches Guidelines.
  * Updates in the %%install section.
  * Removed manpage from the package since it is empty.
  * Minor fixes in %%files section.
- Added the license file from the package's homepage.
- Renamed recoverdm-0.20_cflags.patch to fix_cflags.patch.
- Renamed recoverdm-0.20_fix_gcc_warnings.patch to fix_gcc_warnings.patch.
* Wed Nov 17 2010 asterios.dramis@gmail.com
- Spec file updates after spec-cleaner run.
* Tue Nov 16 2010 asterios.dramis@gmail.com
- Added a patch (recoverdm-0.20_cflags.patch) to make the package use the
  CFLAGS=$RPM_OPT_FLAGS from spec file.
- Used CFLAGS=$RPM_OPT_FLAGS to compile the package.
- Added a patch (recoverdm-0.20_fix_gcc_warnings.patch) to fix some gcc
  compilation warnings that made rpm post-build-checks fail.
* Fri Nov 12 2010 asterios.dramis@gmail.com
- Corrected the release number in the spec file.
* Wed Nov 10 2010 asterios.dramis@gmail.com
- Spec file updates after spec-cleaner run.
* Tue Nov  9 2010 asterios.dramis@gmail.com
- Initial release (version 0.20).
