%undefine _debugsource_packages

Name: wxmathplot
Version: 0.1.2
Release: 9.1
License: wxWindows
Summary: 2D plot library for wxWidgets
Group: Applications/Development
URL: https://wxmathplot.sourceforge.net/
Source: https://sourceforge.net/projects/wxmathplot/files/wxmathplot/%{version}/wxMathPlot-%{version}.tar.gz
BuildRequires: cmake wxGTK2-devel

%description
wxMathPlot is a library to add 2D scientific plot functionality to wxWidgets.
It allows to embed inside your program a window for plotting scientific,
statistical or mathematical data, with additions like legend or coordinate
display in overlay.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n wxMathPlot-%{version}
sed -i '/SET(wxWidgets_USE_LIBS base core)/d' CMakeLists.txt

%build
%cmake -D CMAKE_CXX_COMPILER=g++ -D CMAKE_INSTALL_PREFIX:STRING=/usr -D GDB_DEBUG:BOOL=FALSE -D BUILD_NATIVE:BOOL=TRUE -D MATHPLOT_SHARED:STRING=TRUE -D WXMATHPLOT_BUILD_EXAMPLES:BOOL=FALSE .
%cmake_build

%install
rm -rf %{buildroot}
%cmake_install
%ifarch aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc README Changelog
%{_libdir}/lib*.so

%files devel
%{_includedir}/*
%{_datadir}/wxMathPlot/samples/*
%{_datadir}/wxMathPlot/Doxyfile

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.2
- Rebuilt for Fedora
