Name:           qwinff
Version:        0.1.8
Release:        4.3
Summary:        An intuitive media converter gui
License:        GPLv3
URL:            http://code.google.com/p/qwinff/
Source0:        qwinff_%{version}.tar.bz2
Patch0:         pkgconfig_gtk.patch
Group:          Productivity/Multimedia/Video/Editors and Convertors
BuildRequires:  qt4-devel
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig(libnotify)
Requires:       ffmpeg
Requires:       sox

%description
QWinFF is a cross-platform, easy-to-use media converter frontend to FFmpeg.
FFmpeg is a powerful command-line utility to convert audio and video file
into numerous formats. QWinFF features a rich set of presets to help users
use FFmpeg easily without having to manually input command-line flags.
Average users can convert multiple media files in just a few clicks,
while advanced users can still adjust conversion parameters in detail.

%prep
%setup -q
%patch0

%build
make QMAKE=qmake-qt4 USE_LIBNOTIFY=1 %{?jobs:-j %jobs}

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/qwinff
%{_datadir}/applications/qwinff.desktop
%{_datadir}/pixmaps/qwinff.png
%{_datadir}/qwinff
%{_mandir}/man1/qwinff.1.gz
%doc CHANGELOG.txt COPYING.txt COPYING-v3.txt INSTALL.txt README.txt

%changelog
* Sun Mar 17 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.8
- Rebuilt for Fedora
* Wed Feb 13 2013 - lzh9102@gmail.com
- Update to version 0.1.8
* Fri Aug 31 2012 - lzh9102@gmail.com
- Update Czech translation
* Fri Aug 17 2012 - lzh9102@gmail.com
- New Feature: Shutdown computer when all tasks are done.
- Add several ffmpeg presets that don't give extra arguments.
* Thu Jun 21 2012 - lzh9102@gmail.com
- Update to version 0.1.4
- Minor gui improvements
* Thu Feb 9 2012 - lzh9102@gmail.com
- Updated to version 0.1.2
* Thu Feb 9 2012 - lzh9102@gmail.com
- Initial package, version 0.1.1
