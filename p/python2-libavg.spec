%undefine _debugsource_packages

Name: python2-libavg
Summary: High-level development platform for media-centric applications
Version: 1.8.2git
Release: 1
Group: python
License: Free Software
URL: http://www.libavg.de
Source0: libavg-master.zip
BuildRequires: cmake
BuildRequires: boost-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: pango-devel
BuildRequires: python2-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: librsvg2-devel
BuildRequires: compat-ffmpeg28-devel
BuildRequires: SDL2-devel
BuildRequires: libxml2-devel
BuildRequires: libjpeg-devel

%description
libavg is a high-level development platform for media-centric applications.
It uses an xml-based layout language for screen design and Python as scripting
language. libavg allows developers and media artists/designers to quickly
develop media applications.

%prep
%setup -q -n libavg-master
sed -i 's|PUBLIC base|PUBLIC base ${SDL2_LDFLAGS}|' src/audio/CMakeLists.txt
sed -i '22i #include <iostream>' src/base/ThreadHelper.cpp
sed -i 's| python| python27|' CMakeLists.txt
sed -i -e 's|/usr/bin/python|/usr/bin/python2|' -e 's|/usr/bin/env python|/usr/bin/python2|' `find . -name '*.py'`

%build
cp /usr/share/automake-*/config.guess .
%cmake -DPYTHON_INTERPRETER:FILEPATH=/usr/bin/python2 .
sed -i -e 's|include/ffmpeg|include/compat-ffmpeg28|' -e 's|-lswscale|-L%{_libdir}/compat-ffmpeg28;-lswscale|' CMakeCache.txt
%cmake_build

%install
mkdir -p %{buildroot}%{python2_sitearch} %{buildroot}%{python2_sitelib}
%cmake_install
cd python
python2 setup.py install --root=%{buildroot} --prefix=%{_prefix}
mv %{buildroot}%{python2_sitelib}/* %{buildroot}%{python2_sitearch}

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_bindir}/avg_*
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{python2_sitearch}/libavg/test/Test.py

%files
%doc COPYING README.md NEWS
%{_includedir}/libavg
%{_bindir}/avg_*
%{python2_sitearch}/*

%changelog
* Wed Jan 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.2git
- Regenerated spec using deb2spec
