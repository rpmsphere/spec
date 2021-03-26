Name:           codeslayer
Version:        4.3.1
Release:        5.1
Summary:        A lightweight code editor
License:        GPL
URL:            http://code.google.com/p/codeslayer/
Source0:        http://codeslayer.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  intltool, gtk3-devel, gtksourceview3-devel

%description
CodeSlayer is a source code editor that boasts a clean interface but powerful
features. It is written in C using the GTK+ toolkit.

%package devel
Summary:        Development files of Codeslayer

%description devel
Development files of Codeslayer.

%prep
%setup -q

%build
%configure
#sed -i '1i #include <gtksourceview/gtksourcebuffer.h>' codeslayer/codeslayer-notebook.c codeslayer/codeslayer-notebook-page.c codeslayer/codeslayer-editor.c
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%files
%doc ABOUT-NLS AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_libdir}/lib%{name}.so.*
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Dec 18 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.3.1
- Rebuild for Fedora
