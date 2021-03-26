Name:           gnome-vfs-obexftp
Version:        0.4
Release:        2.2
License:        LGPL v2.1 or later
Summary:        GNOME VFS module for OBEX FTP
Url:            https://launchpad.net/gnome-vfs-obexftp
Group:          Productivity/Networking/File-Sharing
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  bluez-libs-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  expat-devel
BuildRequires:  openobex-devel

%description
GNOME VFS is the GNOME Virtual File System. GNOME VFS abstracts
various operations on files and directories over a collection of
backends.

OBEX is the OBject EXchange protocol. OBEX enables transfer of binary
files over Bluetooth or IrDA (infrared) links.

This package contains a GNOME VFS backend to access remote files over
OBEX FTP, for example mobile phones or personal digital assistants.

%prep
%setup -q

%build
%configure --disable-static \
        --enable-nautilus-workaround
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING COPYING.LIB NEWS README README.unsupported
%{_sysconfdir}/gnome-vfs-2.0/modules/obex-module.conf
%{_libdir}/gnome-vfs-2.0/modules/libobex.so

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Sun Jun 14 2009 vuntz@novell.com
- Clean up package for Contrib.
