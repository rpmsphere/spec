%undefine _debugsource_packages

Summary: SELinux policy analizing
Name: segatex 
Version: 8.640
Release:3.1
License: GPL
Group: Applications/Security
URL: https://sourceforge.net/projects/segatex/
Source: segatex-%{version}.tgz
BuildRequires: gcc-c++, qt-devel, libselinux-devel

%description
segatex is a program even if not knowing much about
SELinux commands, can easily set SELinux commands by GUI.

%prep
%setup -q

%build
cd src
qmake-qt4 -o Makefile segatex.pro
make SUBLIBS='-lselinux'

#cd %{_builddir}/%{name}-%{version}/src/alert
#qmake-qt4 -o Makefile segatex_alert.pro

#cd %{_builddir}/%{name}-%{version}/src/alert_check
#cc -o etc_shadow_check etc_shadow_check.c

%install
rm -rf $RPM_BUILD_ROOT/usr/share/segatex
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/segatex
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/segatex/{refpolicy,images,semanage,aureport,ausearch,seinfo,sesearch,sepolicy}
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/segatex/raw_te_files/{admin,apps,contrib,kernel,roles,services,system}
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/segatex/raw_if_files/{admin,apps,contrib,kernel,roles,services,system}
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/segatex/utils
%{__mkdir} -p $RPM_BUILD_ROOT/usr/{bin,sbin}
%{__mkdir} -p $RPM_BUILD_ROOT/etc/pam.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/rc.d/init.d
%{__mkdir} -p $RPM_BUILD_ROOT/etc/xdg/autostart
%{__mkdir} -p $RPM_BUILD_ROOT/etc/security/console.apps
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/{applications,pixmaps}
%{__mkdir} -p $RPM_BUILD_ROOT/root
#%{__mkdir} -p $RPM_BUILD_ROOT/etc/xdg/autostart

%{__install} %{_builddir}/%{name}-%{version}/src/segatex \
$RPM_BUILD_ROOT/usr/sbin/%{name}
%{__ln_s} /usr/bin/consolehelper \
$RPM_BUILD_ROOT/usr/bin/%{name}
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex_for_consolehelper \
$RPM_BUILD_ROOT/etc/pam.d/%{name}
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex-gui \
$RPM_BUILD_ROOT/etc/security/console.apps/%{name}
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex-gui.desktop \
$RPM_BUILD_ROOT/usr/share/applications/segatex-gui.desktop
%{__install} -m 644 %{_builddir}/%{name}-%{version}/src/images/icon.png \
$RPM_BUILD_ROOT/usr/share/pixmaps/segatex-gui.png

cp -R %{_builddir}/%{name}-%{version}/refpolicy/* \
$RPM_BUILD_ROOT/usr/share/%{name}/refpolicy
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/admin/*.te* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/admin/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/apps/*.te* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/apps/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/contrib/*.te* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/contrib/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/kernel/*.te* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/kernel/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/roles/*.te* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/roles/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/services/*.te \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/services/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/system/*.te* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files/system/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/admin/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/admin/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/apps/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/apps/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/contrib/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/contrib/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/kernel/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/kernel/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/roles/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/roles/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/services/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/services/
cp %{_builddir}/%{name}-%{version}/refpolicy/policy/modules/system/*.if* \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files/system/
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/refpolicy
cp -R %{_builddir}/%{name}-%{version}/src/images/* \
$RPM_BUILD_ROOT/usr/share/%{name}/images
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/images
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/semanage
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/aureport
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/ausearch
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/seinfo
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/sesearch
chmod 700 $RPM_BUILD_ROOT/usr/share/%{name}/sepolicy
%{__install} -m 755 %{_builddir}/%{name}-%{version}/breakte.sh \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files
%{__install} -m 644 %{_builddir}/%{name}-%{version}/all.if all.spt allif.txt allspt.txt splitfile.txt \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_te_files
%{__install} -m 755 %{_builddir}/%{name}-%{version}/breakif.sh \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files
%{__install} -m 644 %{_builddir}/%{name}-%{version}/allif_exclude_myself.txt start_file define_file all.if all.spt allif.txt allspt.txt \
$RPM_BUILD_ROOT/usr/share/%{name}/raw_if_files
%{__install} -m 644 %{_builddir}/%{name}-%{version}/splash.png \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/CONTRIBUTORS \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/HISTORY \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/README \
$RPM_BUILD_ROOT/usr/share/%{name}/
#%{__install} -m 644 %{_builddir}/%{name}-%{version}/README_jp \
#$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/sqlrefpolicy.db \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex.te \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex.if \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex.fc \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/segatex.pp \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/auditcheck2.te \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/auditcheck2.if \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/auditcheck2.fc \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/auditcheck2.pp \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 700 %{_builddir}/%{name}-%{version}/SEGATEX_RPM_POST_INSTALL \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 700 %{_builddir}/%{name}-%{version}/SILENCE_SETROUBLESHOOTD_FOR_SEEPROCESS \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 700 %{_builddir}/%{name}-%{version}/SILENCE_SETROUBLESHOOTD_FOR_SEEPROCESS_END \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 700 %{_builddir}/%{name}-%{version}/DONTAUDIT_STATE \
$RPM_BUILD_ROOT/usr/share/%{name}/
#%{__install} -m 700 %{_builddir}/%{name}-%{version}/utils/getorderedcontextlist \
#$RPM_BUILD_ROOT/usr/share/%{name}/utils
#%{__install} -m 700 %{_builddir}/%{name}-%{version}/utils/classaccessvector \
#$RPM_BUILD_ROOT/usr/share/%{name}/utils
#%{__install} -m 700 %{_builddir}/%{name}-%{version}/utils/booleannames \
#$RPM_BUILD_ROOT/usr/share/%{name}/utils
#%{__install} -m 700 %{_builddir}/%{name}-%{version}/utils/getpidcon \
#$RPM_BUILD_ROOT/usr/share/%{name}/utils
#%{__install} -m 700 %{_builddir}/%{name}-%{version}/utils/selinuxpath \
#$RPM_BUILD_ROOT/usr/share/%{name}/utils
%{__install} -m 700 %{_builddir}/%{name}-%{version}/policygeneration_script \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 644 %{_builddir}/%{name}-%{version}/src/segatex_ja_JP.qm \
$RPM_BUILD_ROOT/usr/share/%{name}/
%{__install} -m 755 %{_builddir}/%{name}-%{version}/downloader/downloader \
$RPM_BUILD_ROOT/usr/share/%{name}/downloader_program
#%{__install} -m 755 %{_builddir}/%{name}-%{version}/src/alert/segatex_alert \
#$RPM_BUILD_ROOT/usr/sbin/segatex_alert
#%{__install} -m 755 %{_builddir}/%{name}-%{version}/src/alert_check/etc_shadow_check \
#$RPM_BUILD_ROOT/usr/sbin/etc_shadow_check
#%{__install} -m 755 %{_builddir}/%{name}-%{version}/etc_shadow_check_script \
#$RPM_BUILD_ROOT/etc/rc.d/init.d/etc_shadow_check_script
#%{__install} -m 644 %{_builddir}/%{name}-%{version}/etc_shadow_check_script_auto.desktop \
#$RPM_BUILD_ROOT/etc/xdg/autostart/etc_shadow_check_script_auto.desktop

%files
/usr/bin/segatex
/usr/sbin/segatex
/etc/pam.d/segatex
/etc/security/console.apps/segatex
/usr/share/applications/segatex-gui.desktop
/usr/share/pixmaps/segatex-gui.png
#/etc/xdg/autostart/segatexauto.desktop
/usr/share/segatex/
#/usr/sbin/segatex_alert
#/usr/sbin/etc_shadow_check
#/etc/rc.d/init.d/etc_shadow_check_script
#/etc/xdg/autostart/etc_shadow_check_script_auto.desktop

%post
/usr/share/segatex/SEGATEX_RPM_POST_INSTALL

%postun
##"$1" = 0 equals "rpm -e segatex"### 
if [ "$1" = 0 ]; then
echo "You said good-bye to segatex."
echo "" 
echo "Cleaing up /usr/share/segatex"
rm -rf /usr/share/segatex
############remove segatex related policies######################################
echo "Removing segatex.pp"
semodule -r segatex
echo "Removing auditcheck2.pp"
semodule -r auditcheck2
############restorcon directory and files affected by segatex#################
echo "restorecon /usr/share"
restorecon -R -v /usr/share
echo "restorecon /usr/sbin"
restorecon -R -v /usr/sbin
echo "restorecon /usr/bin"
restorecon -R -v /usr/bin
echo "" 
############echo messages#################
echo "Uninstalled segatex related files !"
echo "" 
echo "Come back to segatex anytime !"
echo 
fi
exit 0

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 8.640  
- Rebuilt for Fedora
