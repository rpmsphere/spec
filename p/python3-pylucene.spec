Name:           python3-pylucene
Version:        8.1.1
Release:        1
Summary:        Python extension for accessing Java Lucene
Group:          Development/Library
License:        MIT
URL:            http://lucene.apache.org/pylucene/
Source0:        http://apache.stu.edu.tw/lucene/pylucene/pylucene-%{version}-src.tar.gz
BuildRequires:  python3-jcc-devel lua
BuildRequires:  ant python3-devel java-devel-openjdk gcc-c++
BuildRequires:  icu icu4j xml-commons-apis apache-ivy
%define JCC "python3 %{python3_sitearch}/jcc/__init__.py"

%description
PyLucene is a Python extension for accessing Java Lucene. Its goal is to allow
you to use Lucene's text indexing and searching capabilities from Python. It is
designed to be API compatible with the latest version of Java Lucene.

Please note that this version does not use GCJ any more. Instead the Java Native
Interface is used via generated C++ wrapper classes.

%package docs
Summary: PyLucene documentation
Group: Documentation

%description docs
This package contains the documentation and samples for PyLucene.

%prep
%setup -q -n pylucene-%{version}
#sed -i -e /rename/d -e /module/d Makefile
#sed -i 's|i386/client|i386/server|' jcc/setup.py
#sed -i 's|(this.data)|(in)|' lucene-java-%{version}/lucene/core/src/java/org/apache/lucene/codecs/lucene4?/Lucene4?DocValuesProducer.java

%build
cd jcc
JCC_JDK=/usr/lib/jvm/java-openjdk python3 setup.py build
cd ..
LIBDIR_NAME=%{_libdir} PYTHON=python3 INSTALL_ROOT=%{_libdir} PREFIX_PYTHON=/usr JCC=%{JCC} ANT="ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8" NUM_FILES=1 \
    make

%install
cd jcc
python3 setup.py install
cd ..
PYTHON=python3 JCC=%{JCC} ANT="ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.8" NUM_FILES=2 \
	make install INSTALL_OPT="--prefix /usr --root $RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES LICENSE README
%{python3_sitearch}/lucene*

%files docs
%doc samples

%changelog
* Thu Apr 30 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 8.1.1
- Rebuilt for Fedora
* Tue Sep 01 2009 Ciaran Farrell <cfarrell1980@gmail.com> - 2.4.1-2
- First build using idea from Felix Schwarz
