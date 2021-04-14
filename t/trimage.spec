Name:           trimage
Version:        1.0.6
Release:        2
License:        MIT
Summary:        Tool for Losslessly Optimizing PNG and JPEG Files
URL:            http://trimage.org/
Group:          Productivity/Graphics/Other
Source0:        https://github.com/Kilian/Trimage/archive/%{version}.tar.gz#/Trimage-%{version}.tar.gz
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       advancecomp
Requires:       jpegoptim
Requires:       optipng
Requires:       pngcrush
Requires:       python3-qt5
BuildArch:      noarch

%description
Trimage is a cross-platform GUI and command-line interface to optimize
image files via optipng, pngcrush, advpng and jpegoptim, depending on
the filetype (currently, PNG and JPEG files are supported). It was
inspired by imageoptim. All image files are losslessy compressed on
the highest available compression levels. Trimage gives you various
input functions to fit your own workflow: a regular file dialog,
dragging and dropping and various command line options.

%prep
%setup -q -n Trimage-%{version}

%build

%install
python3 setup.py install \
    --root=%{buildroot} \
    --prefix=%{_prefix}

%files
%doc COPYING *.md
%{_bindir}/*
%{python3_sitelib}/*
%{_mandir}/man?/*
%{_datadir}/applications/trimage.desktop
%{_datadir}/icons/hicolor/scalable/apps/trimage.svg

%changelog
* Wed Mar 25 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.6
- Rebuilt for Fedora
* Tue May  1 2012 lazy.kent@opensuse.org
- Removed check for unsupported openSUSE versions.
* Thu Nov 10 2011 lazy.kent@opensuse.org
- Build requires python-setuptools or python-distribute (for
  openSUSE >= 12.1).
- spec clean up.
* Tue Jul 12 2011 lazy.kent@opensuse.org
- Patch to install manual page.
- Added todo to docs.
- Replace JPG with JPEG in summary and description.
* Sun Jul 10 2011 lazy.kent@opensuse.org
- Added manual page.
- Added icon_theme_cache_post/un macros.
* Sun May 29 2011 lazy.kent@opensuse.org
- Initial package created - 1.0.5.
