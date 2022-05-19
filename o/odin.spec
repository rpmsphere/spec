Name: odin
Summary: Develop, simulate and run magnetic resonance sequences
Version: 2.0.5
Release: 1
Group: Science
License: Free Software
URL: http://od1n.sourceforge.net
Source0: http://prdownloads.sourceforge.net/od1n/%{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: qt5-qtbase-devel
BuildRequires: blitz-devel

%description
ODIN is a framework for magnetic resonance imaging (MRI).
It covers the whole toolchain of MRI, from low-level data acquisition
to image reconstruction. In particular, it aims at rapid prototyping
of MRI sequences. The sequences can be programmed using a high-level,
object oriented, C++ programming interface.  It provides advanced
sequence analysis tools, such as interactive plotting of k-space
trajectories, a user interface for a fast compile-link-test cycle
and a powerful MRI simulator which supports different virtual samples.
For fast and flexible image reconstruction, ODIN contains a highly
customizable, multi-threaded data-processing framework.

%prep
%setup -q

%build
%configure
sed -i -e 's|%{_libdir}/qt-3.3/bin|%{_libdir}/qt5/bin|' -e 's|-I/usr/lib64/qt-3.3/include|%(pkg-config --cflags Qt5PrintSupport)|' -e 's|-lqt-mt|%(pkg-config --libs Qt5PrintSupport)|' Makefile */Makefile */*/Makefile
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc TODO README AUTHORS ChangeLog COPYING
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_includedir}/*
%{_libdir}/lib*
%{_mandir}/man1/*.1.*
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Apr 24 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.5
- Rebuilt for Fedora
