%global debug_package %{nil}

Name: btk
Summary: Biomechanical ToolKit
Version: 0.3.0
Release: 16.1
Group: Development/Libraries
License: New BSD License
URL: https://code.google.com/p/b-tk/
Source0: https://b-tk.googlecode.com/files/%{name}-core-%{version}_src.zip
BuildRequires: cmake
BuildRequires: swig
BuildRequires: python2-devel
BuildRequires: atlas numpy

%description
BTK is an open-source and cross-platform library for biomechanical analysis.
BTK read and write acquisition files and can modify them. All these operations
can be done by the use of the C++ API or by the wrappers included (Matlab,
Octave, and Python).

The core of BTK is primary based on a pipeline design and on shared pointers.
Each process can be linked (the output of previous is the input of the next)
and scheduled together. The use of shared pointers permits to avoid the need of
memory allocation/deletion, the choice of object's owner and the possibilities
of memory leaks. Since BTK 0.1.7, the binary files (C3D, TRB, ANB, RIC, etc)
use the memory-mapped file mechanism to be read and written faster (2x and more).

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -c
%ifarch aarch64
sed -i 's|__x86_64__|__aarch64__|' Code/IO/btkBinaryFileStream.h
%endif

%build
%cmake -DBTK_WRAP_PYTHON=off
make %{?_smp_mflags}

%install
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc Copyright.txt Readme.html
%{_libdir}/%{name}*/lib*.so.*
%{_datadir}/%{name}*

%files devel
%{_includedir}/%{name}*
%{_libdir}/%{name}*/lib*.so

%changelog
* Tue Jan 14 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuild for Fedora
