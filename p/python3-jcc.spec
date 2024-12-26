%undefine _debugsource_packages

Name:           python3-jcc
Version:        3.15
Release:        1
Summary:        C++ code generator for calling Java from C++/Python
Group:          Development/Languages
License:        MIT
URL:            https://pypi.python.org/pypi/JCC/
Source0:        https://pypi.python.org/packages/source/J/JCC/JCC-%{version}.tar.gz
Requires:       java-openjdk
BuildRequires:  gcc-c++
BuildRequires:  python3-devel java-devel lua

%description
JCC is a C++ code generator for producing the glue code necessary to call
into Java classes from CPython via Java's Native Invocation Interface (JNI).

JCC generates C++ wrapper classes that hide all the gory details of JNI
access as well Java memory and object reference management.

JCC generates CPython types that make these C++ classes accessible from a
Python interpreter. JCC attempts to make these Python types pythonic by
detecting iterators and property accessors. Iterators and mappings may also
be declared to JCC.

%package devel
Summary: Source code for JCC wrapper classes
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the source code which is needed by JCC to generate 
wrapper classes.

%prep
%setup -q -n jcc-%{version}
#sed -i "s|else 'm'|else ''|" setup.py
#sed -i -e 's|PyUnicode_WCHAR_KIND|PyUnicode_4BYTE_KIND|' -e 's|PyUnicode_AsUnicodeAndSize|PyUnicode_AsUTF8AndSize|' jcc3/sources/JCCEnv.cpp
sed -i 's|jre/lib/amd64|lib|' setup.py

%build
JCC_JDK=/usr/lib/jvm/java-openjdk python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
JCC_JDK=/usr/lib/jvm/java-openjdk python3 setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
 
%files
%doc CHANGES LICENSE README
%{python3_sitearch}/*

%files devel
%{python3_sitearch}/jcc/sources

%changelog
* Sun Nov 17 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 3.15
- Rebuilt for Fedora
* Mon Aug 25 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.9-5
- use environment variables instead of patching setup.py
- compile with -O0 to work around a SIGSEGV in generated code
* Mon Jun 02 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.9-4
- fixed permissions
- moved header files to devel package
* Tue May 27 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.9-3
- renamed package to python-jcc
- removed patch for setup (we can use environment variables)
- added some scripting logic so that the package builds on i386 and x86_64
* Thu May 22 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.9-2
- re-added sources directory as it is needed for compiling PyLucene (-> -devel?)
* Thu May 22 2008 Felix Schwarz <felix.schwarz@oss.schwarz.eu> - 1.9-1
- initial packaging
