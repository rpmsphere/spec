%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Summary: A general purpose open-source plotting and data analysis program
Name: robot
Version: 4.92
Release: 10.2
Source0: http://www.alge.no/ftp/pub/xview/Xview/apps/robotx/%{name}x%{version}.tar.gz
License: open source
URL: http://www.sai.msu.su/sal/D/1/ROBOT.html
Group: Applications/Engineering
BuildRequires: libX11-devel
BuildRequires: xview-devel libtirpc-devel
BuildRequires: compat-gcc-34-g77
BuildRequires: fsplit

%description
XView based scientific graph plotting and data analysis tool. Main Features of Robot:
* Graph plotting in various styles - error bars, histogram, symbols, lines, dashed lines etc. Linear or logarithmic axes.
* Data manipulation - arithmetic, functions, Fourier transforms, smoothing, folding, sorting.
* Fitting to data using built in functions such as Gaussians, polynomials, Lorentzians, and/or a user defined function.
* Annotation of graphs with text in various styles, simple drawing tools.
* Interaction with Robot is via pull-down menus, buttons etc. and/or a pseudo command line type interface.
* Commands are stored in log files for later play back, editing etc.
* Command files can also include basic programming constructs: loops, if tests, user defined variables.
* Multi-color plots. Multiple plots per page. Multiple pages.
* Output in PostScript format.

%prep
%setup -q -n %{name}x%{version}
sed -i 's|static void|void|' Robot/dnd.c
sed -i 's|_IO_||g' Robot/main.c
sed -i 's|-lX11|-lX11 -ltirpc -Wl,--allow-multiple-definition|' Robot/Makefile

%build
make

%install
rm -rf %{buildroot}
install -Dm755 Robot/%{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%doc BUGS README CHANGES
%{_bindir}/%{name}

%changelog
* Sun Apr 07 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 4.92
- Rebuilt for Fedora
