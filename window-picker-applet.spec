%define         schema_name window-picker
Name:           window-picker-applet
Version:        0.2
Release:        1
Summary:        Window picker applet for GNOME
Group:          User Interface/Desktops
License:        GPL
URL:            https://launchpad.net/netbook-remix
Source0:        window-picker-applet_0.2.tar.gz
BuildRequires:  intltool, gettext, pkgconfig
BuildRequires:  GConf2-devel, libgnomeui-devel, libwnck-devel, mate-panel-devel

%description
Window picker applet for GNOME.

%prep
%setup -q
sed -i -e 's/ -Werror/ /' -e 's|libpanelapplet-2.0|libmatepanelapplet-4.0|' configure.ac
sed -i -e 's/GtkTooltip /GtkTooltips /' -e '/gtk_tooltip_set_text/d' -e '/gtk_tooltip_set_icon/d' -e 's/wnck_action_menu_new/wnck_create_window_action_menu/g' src/task-list.c

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/window-picker-applet

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
