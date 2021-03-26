Name: pixelize
Summary: Making mosaics from images
Version: 1.0.0
Release: 3.1
License: GPL
Group: Productivity/Graphics/Other
Source: %{name}-%{version}.tar.bz2
BuildRequires: gtk2-devel gcc
BuildRoot: %{_tmppath}/build-root-%{name}
URL: http://lashwhip.com/pixelize.html

%description
Pixelize works by splitting up the image you want rendered (or duplicated) into
a grid of small rectangular areas. Each area is analyzed, and replaced with an
image chosen from a large database of images. Pixelize tries to pick images that
best match each area.

Pixelize works best when it can choose images from a very large database of images.
With about 1000 images, Pixelize can do a reasonable job. 

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
make -j 2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 755 pixelize $RPM_BUILD_ROOT%{_bindir}
install -m 755 make_db $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,0755)
%doc README LICENSE TODO
%{_bindir}/pixelize
%{_bindir}/make_db

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora
* Wed Jul 15 2009 admin@eregion.de
- initial import: 1.0.0
