%define pyname carray

Name:           python2-%{pyname}
Version:        0.4
Release:        10.1
Summary:        Chunked container for numerical data
License:        BSD
Group:          Development/Libraries/Python
URL:            http://carray.pytables.org/
Source0:        %{pyname}-%{version}.tar.bz2
BuildRequires:  python2-devel, numpy, Cython, atlas-devel
Requires:       numpy

%description
carray is a chunked container for numerical data.  Chunking allows for
efficient enlarging/shrinking of data container.  In addition, it can
also be compressed for reducing memory needs.  The compression process
is carried out internally by Blosc, a high-performance compressor that
is optimized for binary data.

%prep
%setup -q -n %{pyname}-%{version}
sed -i 's|1\.4\.1|1.0|' pavement.py
%ifarch aarch64
sed -i '129,131d' pavement.py
%endif

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt RELEASE_NOTES.txt
%doc LICENSES/BLOSC.txt LICENSES/CARRAY.txt
%{python2_sitearch}/*

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
* Sat Feb 26 2011 ocefpaf@yahoo.com.br
- first OpenSuse release
