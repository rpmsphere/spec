%undefine _debugsource_packages

Name:           tamuanova
Version:        0.2
Release:        13.1
Summary:        Both single and two factor ANOVA
Group:          Productivity/Scientific/Math
License:        GPL-2.0
URL:            https://www.stat.tamu.edu/~aredd/tamuanova/     
Source0:        %{name}-%{version}.tar.bz2
Source1:        %name.CMakeLists.txt
BuildRequires:  gcc-c++ gsl-devel cmake

%description 
ANOVA, or Analysis of Variance, is a method for comparing levels of 
some continuous response variable between different groups. The main 
idea is to compare variation within each group to variation between 
the groups; if the groups vary considerably from one group to another 
in comparison to the within group variation, we can reject the null 
hypothesis that all the groups have similar levels of the response 
variable.

TAMU ANOVA contains both single and two factor ANOVA. Use of the 
package can be facilitated through linking to the compiled library 
tamuanova. The package function definitions are accessible through 
tamu_anova.h

%package        devel
Summary:        Development files for %{name}
Group:          Productivity/Scientific/Math
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -n tamuanova-%version

%build 
cp %{SOURCE1} CMakeLists.txt
cmake -DCMAKE_INSTALL_PREFIX=%_prefix -Dlib=%_libdir
make

%install
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
* Thu Mar  8 2012 aeszter@gwdg.de
- set BuildRoot (required for CentOS)
* Mon Mar  5 2012 aeszter@gwdg.de
- fix changelog name
* Mon Mar  5 2012 aeszter@gwdg.de
- fix various rpmlint warnings
* Mon Mar  5 2012 aeszter@gwdg.de
- omit soversion from devel name
* Thu Feb 16 2012 alinm.elena@gmail.com
- initial commit
