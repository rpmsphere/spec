Summary:	The Ultimate Graphing Calculator
Name:		graphcalc
Version:	0.0.1
Release:	8.1
License:	GPL-2.0+
Group:		Applications/Engineering
URL:		http://www.graphcalc.com/
Source0:	http://prdownloads.sourceforge.net/gcalc/graphcalc-0.0.1.tar.bz2
BuildRequires:  gcc-c++, qt3-devel, ginac-devel, mesa-libGL-devel

%description
Well, no guarantees that I know what I'm doing yet... but here is a semi-stable
release of the development I'm doing on GraphCalc for Linux. Please don't even
attempt using this unless you are decent at installing software on Linux, as the
process is a little tricky. Also, please don't use it for any mission critical
applications.

%prep
%setup -q -n graphcalc

%build
export QTDIR=%{_libdir}/qt-3.3
cd linux
$QTDIR/bin/qmake
sed -i 's|-lginac|-lginac -lGL|' Makefile
make %{?_smp_mflags}
										
%install
rm -rf $RPM_BUILD_ROOT
cd linux
install -Dm755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc TODO README FAQ AUTHORS COPYING
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuilt for Fedora
