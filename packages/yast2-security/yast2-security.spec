#
# spec file for package yast2-security
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-security
Version:        3.2.3
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  perl-XML-Writer
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  yast2-pam
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(yast-rake) >= 0.2.5
# cfg_mail.scr
BuildRequires:  yast2 >= 3.1.179

# new Pam.ycp API
Requires:       yast2-pam >= 2.14.0

# cfg_mail.scr
Requires:       yast2 >= 3.1.179

Provides:       y2c_sec
Provides:       yast2-config-security
Obsoletes:      y2c_sec
Obsoletes:      yast2-config-security
Provides:       y2t_sec
Provides:       yast2-trans-security
Obsoletes:      y2t_sec
Obsoletes:      yast2-trans-security

BuildArch:      noarch

Requires:       yast2-ruby-bindings >= 1.0.0

# Unfortunately we cannot move this to macros.yast,
# bcond within macros are ignored by osc/OBS.
%bcond_with yast_run_ci_tests
%if %{with yast_run_ci_tests}
BuildRequires:  rubygem(yast-rake-ci)
%endif

Summary:        YaST2 - Security Configuration
License:        GPL-2.0
Group:          System/YaST

%description
The YaST2 component for security settings configuration.

%prep
%setup -n %{name}-%{version}

%build

%check
%yast_check

%install
%yast_install

%post
# remove broken entry in /etc/login.defs, introduced during installation (bnc#807099)
if [ -f /etc/login.defs  ] ; then
  sed -e '/^[ \t]*LASTLOG_ENAB[ \t]*\"\"/d' -i /etc/login.defs
fi

%files
%defattr(-,root,root)
%dir %{yast_yncludedir}/security
%{yast_yncludedir}/security/*
%{yast_desktopdir}/security.desktop
%{yast_clientdir}/security*.rb
%{yast_moduledir}/Security.rb
%{yast_scrconfdir}/*.scr
%{yast_schemadir}/autoyast/rnc/security.rnc
%{yast_ydatadir}/security
%{yast_libdir}/security
%doc %{yast_docdir}

%changelog
