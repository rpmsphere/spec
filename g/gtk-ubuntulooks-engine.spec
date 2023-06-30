%define _name ubuntulooks

Name: gtk-%{_name}-engine
Version: 0.9.12
Release: 3.1
Summary: Ubuntulooks GTK2 engine
Summary(ru_RU.UTF-8):Модуль прорисовки Ubuntulooks для GTK2
License: GPL
Group: Graphical desktop/GNOME
URL: https://www.gnome-look.org
Source0: %{_name}_%{version}.orig.tar.gz
BuildRequires: gcc-c++ gtk2-devel

%description
Ubuntulooks is an engine forked from Clearlooks 2.7 to bring a unique look
to Ubuntu.

%description -l ru_RU.UTF-8
Ubuntulooks - самостоятельный вариант Clearlooks 2.7, созданный для придания
уникального внешнего вида дистрибутиву Ubuntu.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure 
make

%install
%make_install

%files
%doc AUTHORS README ChangeLog
%{_libdir}/gtk-2.0/2.10.0/engines/*.so
%exclude %{_datadir}/themes/Human/gtk-2.0/gtkrc
%exclude %{_libdir}/gtk-2.0/2.10.0/engines/*.la

%changelog
* Mon Jul 18 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.12
- Rebuilt for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.9.11-alt1.qa1
- NMU: rebuilt for debuginfo.
* Wed Dec 06 2006 Vyacheslav Dikonov <slava@altlinux.ru> 0.9.11-alt1
- ALTLinux build
