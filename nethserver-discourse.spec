Summary: nethserver-discourse  is a skeleton for a new module
%define name nethserver-discourse
Name: %{name}
%define version 0.0.3
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: git 
Requires: nethserver-docker
BuildRequires: nethserver-devtools
BuildArch: noarch

%description
Discourse is modern forum software for your community. Use it as a mailing list, discussion forum, long-form chat room, and more!


%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/

rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
> %{name}-%{version}-%{release}-filelist

%post

%postun
if [ $1 == 0 ] ; then
    /usr/bin/rm -f /etc/httpd/conf.d/zzz_discourse.conf
    /usr/bin/systemctl reload httpd
fi

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update
%doc COPYING

%changelog
* Wed Aug 04 2021 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.3
- Set the RequestHeader needed when discourse forces the https
- https://community.nethserver.org/t/nethserver-discourse-lets-encrypt-and-ssl/18591/10
- Thank michel andré

* Sat Jul 04 2020 stephane de Labrusse <stephdl@de-labrusse.fr> 0.0.2
- Remove http templates after rpm removal

* Tue May 09 2017 stephane de Labrusse <stephdl@de-labrusse.fr>
- initial
