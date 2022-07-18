%global __os_install_post %{nil}
%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Name:		webmcp
Version:	1.2.5
Release:	1
Summary:	Web application framework in Lua
License:	MIT/X11
Group:		Productivity/Networking
Source0:	http://www.public-software-group.org/pub/projects/%{name}/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:	libpq-devel
BuildRequires:  postgresql-server-devel
BuildRequires:	lua-devel
URL:		http://www.public-software-group.org/webmcp

%description
WebMCP is web application framework written in Lua and C. Instead of using
the classical Model-View-Controller (MVC) concept, WebMCP makes use of a
so-called Model-View-Action concept. The database is accessed through the
Model layer, which provides an Object-Relational Mapping (ORM). HTTP-GET
requests are handled by Views, which process the request data, query the
database, and render the result. HTTP-POST requests are handled by Actions,
which can write to the database and redirect to a View, dependent on success
or failure.

%prep
%setup -q -n %{name}-v%{version}
sed -i -e 's|include/postgresql|include/pgsql|g' -e 's|/usr/lib|%{_libdir}|' Makefile.options
sed -i -e 's|ln -s -f ../../|cp |' -e '/make documentation/d' Makefile

%build
make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/opt/%{name}
%__cp -a framework/* %{buildroot}/opt/%{name}

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE
/opt/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.5
- Rebuilt for Fedora
