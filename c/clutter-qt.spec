# 
# Do not Edit! Generated by:
# spectacle version 0.15
# 
# >> macros
# << macros

Name:       clutter-qt
Summary:    Clutter integration library for QT
Version:    0.9_20090720
Release:    8.7
Group:      System/Libraries
License:    LGPLv2+
URL:        http://www.clutter-project.org/
Source0:    http://www.clutter-project.org/sources/%{name}/0.9/%{name}-%{version}.tar.bz2
Source100:  clutter-qt.yaml
Source200:  clutter-qt-rpmlintrc
Patch0:     clutter-1.0-dependency.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  qt-devel

%description
Description: %{summary}


%package devel
Summary:    Clutter-qt header files and development libraries
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}


%prep
%setup -q -n %{name}-%{version}

# clutter-1.0-dependency.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre

# Do not launch ./autogen.sh in order to avoid double configure run.
autoreconf -v --install || exit 1
%configure --disable-static --prefix=/usr --with-moc=/usr/bin/moc-qt4
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%makeinstall

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libclutter-qt*so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/*
%{_libdir}/pkgconfig/clutter-qt*.pc
%{_libdir}/libclutter-qt-*.so
%{_libdir}/libclutter-qt-0.9.la
# << files devel

%clean
rm -rf %{buildroot}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Jun 15 2010 dimstar@opensuse.org
- Do not run autogen.sh, as it triggers a configure call which does
  not contain all the parameters we want to pass with %%configure,
  and adding all the items is too error prone. Thus we call
  autoreconf and then %%configure manually.
* Mon Jun 14 2010 awafaa@opensuse.org
- Fix autogen line
- Add rpmlintrc (for now)
* Wed Jun  9 2010 awafaa@opensuse.org
- Initial import for openSUSE version 0.9_20090720