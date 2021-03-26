%global		debug_package %{nil}
%define         _name Q7Basic
%define         dest_dir %{_libdir}/Q7Basic

Name:           q7basic
Summary:        Basic for Qt IDE, runtime, compiler and designer
Version:        1.0
Release:        16
URL:            http://www.q7basic.org/
License:        GPL-3.0
Group:          Development/Tools/IDE
BuildRequires:  libtool pkgconfig
BuildRequires:  automake autoconf
BuildRequires:  pkgconfig(QtCore) >= 4.8.0 pkgconfig(QtGui) >= 4.8.0
BuildRequires:  pkgconfig(QtSql) >= 4.8.0
BuildRequires:  pkgconfig(QtWebKit) >= 4.8.0
BuildRequires:  pkgconfig(phonon)
BuildRequires:  pkgconfig(QtNetwork) >= 4.8.0
BuildRequires:  pkgconfig(QtSvg) >= 4.8.0
BuildRequires:  pkgconfig(QtDeclarative) >= 4.8.0
BuildRequires:  pkgconfig(QtXml) >= 4.8.0
Source0:        http://www.q7basic.org/Q7Basic_Source_Code.zip
Source1:        %{name}.png
Source2:        %{_name}.desktop
Patch:          %{_name}-abuild.patch

%description
Q7Basic (KBasic2) is a programming language related to VB.NET, Visual Basic, Visual Basic
for Application and Java. It combines the best features of those tools and
comes with built-in backward support for those tools and QBasic as it is 100%%
syntax compatible to VB6, VBA and QBasic. Additionally, it comes with support
for VB.NET syntax, functions and similar objects and classes. KBasic uses Qt as
its toolkit. Supports PostgreSQL, SQLite, MySQL, ODBC, MPEG, MP3, WebKit, SVG,
C/C++ libraries, stylesheets, multi-platform.
Source codes (Compiler + Runtime + IDE) including documentation and examples
Released under the terms of the GPL3 as published by the Free Software Foundation
If you are interested in using the source codes for other licenses or commercial development, you must buy commercial licenses from KBasic Software.
Please contact the author(s). 
Author: Bernd Noetscher

%package examples
Summary:        Examples to develop with Q7Basic
License:        GPL-3.0
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
BuildArch:	noarch

%description examples
Q7Basic (KBasic2) is a programming language related to VB.NET, Visual Basic, Visual Basic
for Application and Java. It combines the best features of those tools and
comes with built-in backward support for those tools and QBasic as it is 100%%
syntax compatible to VB6, VBA and QBasic. Additionally, it comes with support
for VB.NET syntax, functions and similar objects and classes. KBasic uses Qt as
its toolkit. Supports PostgreSQL, SQLite, MySQL, ODBC, MPEG, MP3, WebKit, SVG,
C/C++ libraries, stylesheets, multi-platform.
Author: Bernd Noetscher

%prep
%setup -q -n Q7Basic_Source_Code
%patch -p1
%__sed -i -e '/#include(Q7BFormDesigner.pri)/s/^#//' \
       -e '/#include(Q7BZipUnzip.pri)/s/^#//' \
       -e '$aLIBS += -lz' ./Q7Basic.pro
%__sed -i -e '\|SOURCES += Q7BFormDesigner/main.cpp|s/^/#/' Q7BFormDesigner.pri

%build
rm moc*
#qmake-qt4 ./Q7Basic.pro QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags} -std=gnu++98 -fpermissive" QMAKE_CXXFLAGS-="-pipe"
qmake-qt4 ./Q7Basic.pro QMAKE_CXXFLAGS+="-std=gnu++98 -fpermissive" QMAKE_CXXFLAGS-="-pipe"
make VERBOSE=0
#qmake-qt4 ./Q7BCompiler.pro QMAKE_CFLAGS+="%{optflags}" QMAKE_CXXFLAGS+="%{optflags} -std=gnu++98" QMAKE_CXXFLAGS-="-pipe"
qmake-qt4 ./Q7BCompiler.pro QMAKE_CXXFLAGS+="-std=gnu++98" QMAKE_CXXFLAGS-="-pipe"
sed -i 's|-O2|-O|' Makefile
make VERBOSE=0

%install
%__install -d %{buildroot}%{_bindir}
%__install -D -m755 Q7Basic %{buildroot}%{dest_dir}/Q7Basic
%__install -m755 Q7BCompiler %{buildroot}/%{dest_dir}/
cp -r body-Dateien Examples Resources Templates test2 %{buildroot}/%{dest_dir}/
cp -p *.txt *.html Q7BRuntime.cpp Q7BRuntime.h *.pdf style.css \
 ExampleBrowserNoDescriptionYet.jpg windows_application_icon.res %{buildroot}/%{dest_dir}/
%__ln_s %{dest_dir}/Resources/{License,Readme}.txt .
%__ln_s %{dest_dir}/Q7Basic %{buildroot}%{_bindir}/%{name}
%__ln_s %{dest_dir}/Q7BCompiler %{buildroot}%{_bindir}/q7bcompiler
install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc License.txt Readme.txt
%{_bindir}/*
%{dest_dir}
%exclude %{dest_dir}/Examples
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files examples
%{dest_dir}/Examples

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
* Sat Sep 14 2013 fa0sck@gmail.com
- Build version 1.0 for openSUSE
