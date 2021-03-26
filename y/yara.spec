Name:           yara
Version:        3.2.0
Release:        4.1
Summary:        A malware identification and classification tool
License:        Apache-2.0
Group:          System/Filesystems
URL:            http://plusvic.github.io/yara/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  file-devel
BuildRequires:  pcre-devel
BuildRequires:  python-devel
#BuildRequires:  jansson-devel

%description
YARA is a tool aimed at helping malware researchers to identify and classify
malware samples. With YARA you can create descriptions of malware families
based on textual or binary patterns contained on samples of those families.
Each description consists of a set of strings and a Boolean expression which
determines its logic.

%package -n libyara
Summary:        Library to support the yara malware identification tool
Group:          System/Libraries

%description -n libyara
YARA is a tool aimed at helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families based on textual or binary patterns contained on samples of those families. Each description consists of a set of strings and a Boolean expression which determines its logic. Let's see an example:

%package -n python-%name
Summary:        Python bindings to support the yara malware identification tool
Group:          Development/Libraries/Python
Requires:	python

%description -n python-%name
YARA is a tool aimed at helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families based on textual or binary patterns contained on samples of those families. Each description consists of a set of strings and a Boolean expression which determines its logic. Let's see an example:

%package -n libyara-devel
Summary:        Development files to support the yara malware identification tool
Group:          Development/Libraries/C and C++
Requires:       libyara = %{version}-%{release}

%description -n libyara-devel
YARA is a tool aimed at helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families based on textual or binary patterns contained on samples of those families. Each description consists of a set of strings and a Boolean expression which determines its logic. Let's see an example:

%prep
%setup -q

%build
./bootstrap.sh
%configure --enable-magic --disable-cuckoo
make %{?_smp_mflags}
cd yara-python
sed -i "/libraries=\['yara'\],/a         library_dirs=['%_builddir/%name-%version/libyara/.libs']," setup.py
python setup.py build

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name '*.la' -delete -print
find %{buildroot} -type f -name '*.a' -delete -print
cd yara-python
python setup.py install --root=%{buildroot} --prefix=%{_prefix}

%post   -n libyara -p /sbin/ldconfig
%postun -n libyara -p /sbin/ldconfig

%files
%doc COPYING README.md CONTRIBUTORS AUTHORS
%{_bindir}/yara
%{_bindir}/yarac
%{_mandir}/man1/yara.1.gz
%{_mandir}/man1/yarac.1.gz

%files -n libyara
%doc COPYING README.md CONTRIBUTORS AUTHORS
%{_libdir}/libyara.so.*

%files -n python-%name
%doc COPYING README.md CONTRIBUTORS AUTHORS docs
%{python_sitearch}/yara_python-*.egg-info
%{python_sitearch}/yara.so

%files -n libyara-devel
%doc COPYING README.md CONTRIBUTORS AUTHORS docs
%{_includedir}/yara.h
%{_includedir}/yara
%{_libdir}/libyara.so

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.0
- Rebuild for Fedora
* Wed Sep 24 2014 Greg.Freemyer@gmail.com
- update to v3.1.0
  * Yara now supports plugin modules
  * Numerous major improvements.  See README.md in the documentation folder for details
- update License to Apache 2.0
- build with cuckoo and magic modules (cuckoo only for factory and newer)
- major specfile cleanup
  * add soname as a variable and use it appropriately
  * add /usr/bin/yarac and associated man file
  * update Url and Source fields
  * add libtool build requirement
  * delete no longer needed patch, now upstream: yara-fixes.patch
  * add ./bootstrap.sh call to %%build section as recommended by upstream
  * add +%%{_includedir}/yara to -devel since it is full of yara related header files
  * use default naming for devel sub-project
  * remove *.a and *.la files from the devel sub-project
  * incorporate python-yara as a sub-project
* Wed Feb 15 2012 Greg.Freemyer@gmail.com
- Release should have a value of zero in OBS.  It is handled automatically via OBS.
* Mon Feb 13 2012 Greg.Freemyer@gmail.com
- use %%{__make} macro
* Thu Feb  9 2012 meissner@suse.com
- built with default compile flags, fixed 2 small issues
* Tue Feb  7 2012 Greg.Freemyer@gmail.com
- Initial submission
  A malware identification and classification tool
