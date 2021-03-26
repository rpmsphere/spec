Name:           qxv
Version:        0.2
Release:        7.1
Summary:        Modern Rewrite of the Classic "xv"
License:        GPL-2.0
Group:          Productivity/Graphics/Viewers
URL:            http://labs.freehackers.org/projects/qxv/
Source0:        http://labs.freehackers.org/attachments/download/422/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRequires:  desktop-file-utils
BuildRequires:  qt-devel

%description
qxv is a basic image viewer, with an interface as close as possible to the old
and unmaintained xv. It is a modern rewrite of the classic "xv".

%prep
%setup -q

%build
qmake-qt4 QMAKE_CXXFLAGS+="%{optflags}" -config release qxv.pro
make %{?_smp_mflags}

%install
install -Dpm 0755 qxv %{buildroot}%{_bindir}/qxv
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%doc COPYING README
%{_bindir}/qxv
%{_datadir}/applications/qxv.desktop

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Mon Aug 27 2012 asterios.dramis@gmail.com
- Use desktop-file-utils instead of deprecated %%suse_update_desktop_file macro
  for installing the desktop file. Replaced update-desktop-files build
  requirement with desktop-file-utils for this.
* Sun Aug 26 2012 asterios.dramis@gmail.com
- Spec file cleanup.
* Sat Oct  1 2011 asterios.dramis@gmail.com
- Spec file updates:
  * Changes based on spec-cleaner run.
  * Changed License: to GPL-2.0.
  * Small changes in summary and description.
  * Updated Url.
  * Changed Group: to Productivity/Graphics/Viewers.
  * Compiled package with RPM_OPT_FLAGS (fix post build check warning).
- Added a desktop file.
* Mon Jan 31 2011 abrouwers@gmail.com
- Update to 0.2
  * Selection using rubberband
  * Cropping support ("c")
  * Auto-resizing image when re-sizing window
  * Middle-mouse button display of pixel information
  * Various bug-fixes
* Tue Oct  5 2010 abrouwers@gmail.com
- version 0.1
  Initial release
