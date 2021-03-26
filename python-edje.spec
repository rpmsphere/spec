Summary:	A collection python of tools for E17
Name:		python-edje
Version:	0.7.3
Release:	20101225
Source0:	%{name}-%{version}.tar.gz
License:	GPL
Group:		Graphical desktop/Enlightenment
URL:		http://www.enlightenment.org/
BuildRequires:	Cython
BuildRequires:	python-evas
Requires:	python >= 2.6


%description
Python support files for Edje

%package devel
Summary: Headers and development libraries from %{name}
Group: Graphical desktop/Enlightenment
Requires: %name = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%setup -q

%build
%configure --disable-static --prefix=/usr
%__make edje/edit/c_edit.c
sed -i '1i typedef struct {\nconst char *program_name;\nint line;\nconst char *error_str;\n} Edje_Edit_Script_Error;' edje/edit/c_edit.c
%__make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf %{buildroot}

%files
%doc README
%_libdir/python*/site-packages/
%{_datadir}/python-edje/examples/01-swallow.edc
%{_datadir}/python-edje/examples/01-swallow.py*
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/01-app_launcher.edc
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/01-app_launcher.py*
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/audio_player.png
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/background.jpeg
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/image_viewer.png
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/video_player.png
%{_datadir}/python-edje/examples/evas-demo/01-app_launcher/web_browser.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/02-vkbd.edc
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/02-vkbd.py*
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/background.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/backspace-selected.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/backspace.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/key-default-selected.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/key-default.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/key-special-selected.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/key-special.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/keyboard-background.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/shift-selected.png
%{_datadir}/python-edje/examples/evas-demo/02-vkbd/shift.png
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/03-kinetic_list.edc
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/03-kinetic_list.py*
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/background.png
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/listitem.png
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_1.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_2.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_3.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_4.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_5.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_6.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_7.jpg
%{_datadir}/python-edje/examples/evas-demo/03-kinetic_list/thumb_8.jpg

%files devel
%{_includedir}/python-edje/edje/__init__.py*
%{_includedir}/python-edje/edje/c_edje.pxd
%{_includedir}/python-edje/edje/edit/__init__.py*
%{_includedir}/python-edje/edje/edit/c_edit.h
%{_includedir}/python-edje/edje/edit/c_edit.pxd
%{_includedir}/python-edje/edje/edje.c_edje.h
%{_libdir}/pkgconfig/python-edje.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Jan 04 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
