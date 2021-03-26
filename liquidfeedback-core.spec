%global debug_package %{nil}
%define _name liquid_feedback_core

Name:		liquidfeedback-core
Version:	2.2.3
Release:	1
Summary:	Interactive Democracy Core
License:	MIT/X11
Group:		Productivity/Networking
Source0:	http://www.public-software-group.org/pub/projects/liquid_feedback/backend/v%{version}/%{_name}-v%{version}.tar.gz
BuildRequires:	lighttpd
BuildRequires:	postgresql-devel
Requires:	lighttpd
Requires:	postgresql-server
URL:		http://liquidfeedback.org/

%description
LiquidFeedback is an open-source software, powering internet platforms for
proposition development and decision making.

The core consists of a database scheme for the PostgreSQL database, including
the algorithms for delegations, feedback and the voting procedure implemented
as SQL views and database procedures written in PL/pgSQL.

%prep
%setup -q -n %{_name}-v%{version}

%build
make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/opt/%{_name}
%__cp *.sql lf_update %{buildroot}/opt/%{_name}

%post
service postgresql initdb
service postgresql restart
su - postgres -c "createuser -S -d -R lighttpd"
su - postgres -c "createdb -O lighttpd liquid_feedback"
su - postgres -c "createlang plpgsql liquid_feedback"
su - postgres -c "psql -v ON_ERROR_STOP=0 -f /opt/%{_name}/core.sql liquid_feedback"
su - postgres -c "psql -v ON_ERROR_STOP=0 -f /opt/%{_name}/init.sql liquid_feedback"
su - postgres -c "/opt/%{_name}/lf_update dbname=liquid_feedback"

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE README
/opt/%{_name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.3
- Rebuild for Fedora
