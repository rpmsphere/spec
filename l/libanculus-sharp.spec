Summary: Reusable utility library written in C#
Name: libanculus-sharp
Version: 0.3.1
Release: 2
Source0: %{name}-%{version}.tar.bz2
Patch: libanculus-sharp-0.3.1-libdir.patch
License: MIT
Group: Development/Libraries
URL: http://code.google.com/p/libanculus-sharp/
Requires: mono-core mono-devel gtk-sharp2
BuildRequires: mono-core mono-devel gtk-sharp2 glib2-devel
BuildArch: noarch

%description
Anculus means servant in Latin, and that is exactly what the library does. It
serves and helps you to easily and quickly write new applications.
libanculus-sharp contains all the building blocks that you need to develop a
good C# application.
Features:
* XML Configuration files (primitive types, strings, serializable objects,
  lists, arrays, ...)
* Sorting algorithms (quicksort)
* String Search algorithms (Boyer-Moore, Aho-Corasick)
* Translation support (Managed Gettext)
* Logging (Console, Colored Console, File)
* Gui thread dispatching (Gtk-sharp, System.Windows.Forms)
* Collections (sorted list) 

%package devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name}

%description devel
This package contains the API files for %{name}.

%prep
%setup -q
%patch -p1

%build
sh autogen.sh --libdir=%{_prefix}/lib
%__make

%install
rm -rf %{buildroot}
%makeinstall pkgconfigdir=%{buildroot}%{_datadir}/pkgconfig
rm -fr %{buildroot}%{_prefix}/lib*/libanculus-sharp

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS
%{_prefix}/lib/mono/libanculus-sharp
%{_prefix}/lib/mono/gac/Anculus.Core/
%{_prefix}/lib/mono/gac/Anculus.Core.Extended/
%{_prefix}/lib/mono/gac/Anculus.Gui/

%files devel
%{_datadir}/pkgconfig/*.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Wed Apr 22 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.3.1-2.ossii
- Rebuild for OSSII

* Fri Jun 20 2008 Götz Waschk <waschk@mandriva.org> 0.3.1-2mdv2009.0
+ Revision: 227504
- fix libdir in pkgconfig files

* Fri Jun 20 2008 Götz Waschk <waschk@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 227459
- fix buildrequires
- fix description
- import libanculus-sharp
