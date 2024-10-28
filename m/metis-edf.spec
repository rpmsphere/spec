Name:           metis-edf
Version:        4.1
Release:        15.1
Summary:        Serial Graph Partitioning and Fill-reducing Matrix Ordering
Group:          Productivity/Graphics/3D Editors
License:        GPL
URL:            https://www.code-aster.org/V2/spip.php?rubrique1
Source0:        metis-edf-4.1-2.noarch.tar.bz2
Patch0:         metis-edf-4.1-2-configure.patch
Patch1:         metis-edf-4.1-2-Makefile.patch
Patch2:         metis-edf-4.1-no-return-in-non-void-fix.patch
BuildRequires:  gcc-gfortran
Requires:       lib%{name} >= %{version}-%{release}

%description
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on the state-of-the-art multilevel paradigm that has been
shown to produce high quality results and scale to very large problems. 

This is a modified version of Metis for Code-Aster.

%package -n libmetis-edf
Summary:        Shared libraries for metis-edf
Group:          System/Libraries

%description -n libmetis-edf
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on the state-of-the-art multilevel paradigm that has been
shown to produce high quality results and scale to very large problems. 

This is a modified version of Metis for Code-Aster.

%package -n libmetis-edf-devel
Summary:        Development files metis-edf
Group:          Development/Libraries/C and C++
Requires:       lib%{name} >= %{version}-%{release}

%description -n libmetis-edf-devel
METIS is a family of programs for partitioning unstructured graphs and hypergraph
and computing fill-reducing orderings of sparse matrices. The underlying algorithms
used by METIS are based on the state-of-the-art multilevel paradigm that has been
shown to produce high quality results and scale to very large problems. 

This is a modified version of Metis for Code-Aster.

%package doc
Summary:        Manual for metid-edf
Group:          Documentation
BuildArch:      noarch

%description doc
This package contains the metis-edf manual in ps fo%__rmat.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1
%patch 2 -p1

%build
export SUSE_ASNEEDED=0
make CFLAGS="$RPM_OPT_FLAGS -Wno-format-security"

%install
%__install -d $RPM_BUILD_ROOT%{_bindir}
%__install -m755 pmetis $RPM_BUILD_ROOT%{_bindir}
%__install -m755 kmetis $RPM_BUILD_ROOT%{_bindir}
%__install -m755 onmetis $RPM_BUILD_ROOT%{_bindir}
%__install -m755 onmetis.exe $RPM_BUILD_ROOT%{_bindir}

strip $RPM_BUILD_ROOT%{_bindir}/[pk]metis
strip $RPM_BUILD_ROOT%{_bindir}/onmetis.exe

%__install -d $RPM_BUILD_ROOT%{_libdir}
%__install -m755 libmetis-edf.so.4.1 $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} %{_libdir}/libmetis-edf.so.4.1 $RPM_BUILD_ROOT%{_libdir}/libmetis-edf.so.4

%__install -d $RPM_BUILD_ROOT%{_libdir}
ln -sf %{_libdir}/libmetis-edf.so.4 $RPM_BUILD_ROOT%{_libdir}/libmetis-edf.so

%post -n lib%{name}
/sbin/ldconfig

%postun -n lib%{name}
/sbin/ldconfig

%files
%doc CHANGES FILES README_Code_Aster VERSION
%{_bindir}/*

%files -n lib%{name}
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%{_libdir}/lib%{name}.so

%files doc
%doc Doc/manual.ps

%changelog
* Tue Dec 13 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1
- Rebuilt for Fedora
* Sun Feb 27 2011 scorot@gtt.fr - 4.1
- first release
