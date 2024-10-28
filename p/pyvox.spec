Name:           pyvox
Version:        0.71
Release:        25.1
Summary:        A set of software tools for medical image processing
Group:          Applications/Multimedia
License:        open source
URL:            https://www.med.upenn.edu/bbl/pyvox.html
Source0:        https://www.med.upenn.edu/bbl/assets/user-content/documents/%{name}-%{version}.src.tgz
BuildRequires:  python2-devel
BuildRequires:  tk-devel

%description
Pyvox is a set of software tools being developed for medical image processing
with a particular emphasis on brain masking and segmentation of magnetic
resonance brain images; tools to support other applications may be added later.
These tools are intended to support researchers who need to prototype new image
analysis algorithms or to develop automated image analysis tools for specific
image analysis applications. The particular sequence of processing operations
is specified through a scripting language which can be used interactively or
in command files; the language used is an extension of Python.

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package contains the development files for %{name}.

%package -n python2-%{name}
Group: Development/Libraries
Summary: pyvox python2 bindings
Requires: %{name} = %{version}-%{release}

%description -n python2-%{name}
This package contains python2 bindings for pyvox.

%prep
%setup -q
sed -i 's|stderr, errm_msg|stderr, "%s", errm_msg|' src/errm.c
sed -i 's|mode->dump, f|mode->dump, "%s", f|' src/exim.c
sed -i 's|Tk_PhotoPutZoomedBlock(pytk->handle|Tk_PhotoPutZoomedBlock(pytk->interp, pytk->handle|' src/tkphoto.c
sed -i 's|xzoom, yzoom, xsubsamp, ysubsamp|xzoom, yzoom, xsubsamp, ysubsamp, TK_PHOTO_COMPOSITE_OVERLAY|' src/tkphoto.c
sed -i 's|/usr/bin/env python|/usr/bin/python2|' scripts/pycompile

%build
%configure --with-python=/usr/bin/python2
make

%install
rm -rf %{buildroot}
for i in %{_bindir} %{_libdir} %{python2_sitearch}/%{name} %{_includedir} /usr/man/man1 /usr/man/man5 %{_datadir} /usr/lib
do
mkdir -p %{buildroot}$i
done
%makeinstall PYSITE=%{buildroot}%{python2_sitearch}/%{name}
mv %{buildroot}/usr/man %{buildroot}%{_mandir}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib/* %{buildroot}%{_libdir}
%endif
chmod +x %{buildroot}%{_libdir}/*
mv %{buildroot}%{_bindir}/regedit %{buildroot}%{_bindir}/regedit-%{name}
mv %{buildroot}%{_mandir}/man1/regedit.1 %{buildroot}%{_mandir}/man1/regedit-%{name}.1

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%{_bindir}/*
%{_libdir}/lib*
%{_mandir}/man?/*
%doc NEWS Credits COPYING README TODO

%files devel
%{_includedir}/*.h

%files -n python2-%{name}
%{python2_sitearch}/%{name}

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.71
- Rebuilt for Fedora
