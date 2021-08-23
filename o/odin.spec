Name: odin
Summary: develop, simulate and run magnetic resonance sequences
Version: 2.0.4
Release: 3
Group: science
License: Free Software
URL: http://od1n.sourceforge.net
Source0: https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
sed -i 's|/moc|/moc-qt5|' configure

%build
%configure
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
* Fri Aug 06 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.4
- Rebuilt for Fedora
