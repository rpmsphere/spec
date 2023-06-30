Name:           flo
Version:	svn1011
Release:	12.1
License:	GPL-2.0+	
Summary:	A mindmap tool with a focus on presentations
URL:		https://trac.geiseri.com/wiki/FloMain
Group:		Productivity/Office/Organizers
Source:		%{name}-%{version}.tar.bz2
Patch1:		%{name}-%{version}-hunspell-path.patch
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++ qt4-devel
BuildRequires:	aspell-devel
BuildRequires:	hunspell-devel
BuildRequires:	doxygen
BuildRequires:	pkgconfig
BuildRequires:	desktop-file-utils

%description
Flo is a multi-platform mind mapping program with a focus on presentations.
One of the main ideas of Flo is to take brainstorms and create outlines and
various documents.

%prep
%setup -q
%patch1 -p1
sed -i '1i #include <unistd.h>' library/sxfile/getusername.cpp

%build
qmake-qt4
make %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS"

%install
rm -f -r $RPM_BUILD_ROOT
%makeinstall INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%doc TODO AUTHORS
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*.xpm

%clean
rm -f -r $RPM_BUILD_ROOT

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - svn1011
- Rebuilt for Fedora
* Sun Feb 12 2012 i@marguerite.su
- initial package svn1011
