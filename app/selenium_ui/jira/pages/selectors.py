from selenium.webdriver.common.by import By
from util.conf import JIRA_SETTINGS


class PopupLocators:
    default_popup = '.aui-message .icon-close'
    popup_1 = 'form.tip-footer>.helptip-close'
    popup_2 = '.aui-inline-dialog-contents .cancel'


class UrlManager:

    def __init__(self, issue_key=None, issue_id=None, project_key=None, jql=None, projects_list_page=None,
                 board_id=None):
        self.host = JIRA_SETTINGS.server_url
        self.login_params = '/login.jsp'
        self.logout_params = '/logoutconfirm.jsp'
        self.dashboard_params = '/secure/Dashboard.jspa'
        self.issue_params = f"/browse/{issue_key}"
        self.project_summary_params = f"/projects/{project_key}/summary"
        self.jql_params = f"/issues/?jql={jql}"
        self.edit_issue_params = f"/secure/EditIssue!default.jspa?id={issue_id}"
        self.edit_comments_params = f"/secure/AddComment!default.jspa?id={issue_id}"
        self.projects_list_params = f'/secure/BrowseProjects.jspa?selectedCategory=all&selectedProjectType=all&page=' \
                                    f'{projects_list_page}'
        self.boards_list_params = '/secure/ManageRapidViews.jspa'
        self.scrum_board_backlog_params = f"/secure/RapidBoard.jspa?rapidView={board_id}&view=planning"
        self.scrum_board_params = f"/secure/RapidBoard.jspa?rapidView={board_id}"

    def login_url(self):
        return f"{self.host}{self.login_params}"

    def dashboard_url(self):
        return f"{self.host}{self.dashboard_params}"

    def issue_url(self):
        return f"{self.host}{self.issue_params}"

    def project_summary_url(self):
        return f"{self.host}{self.project_summary_params}"

    def jql_search_url(self):
        return f"{self.host}{self.jql_params}"

    def edit_issue_url(self):
        return f"{self.host}{self.edit_issue_params}"

    def edit_comments_url(self):
        return f"{self.host}{self.edit_comments_params}"

    def projects_list_page_url(self):
        return f"{self.host}{self.projects_list_params}"

    def boards_list_page_url(self):
        return f"{self.host}{self.boards_list_params}"

    def scrum_board_backlog_url(self):
        return f"{self.host}{self.scrum_board_backlog_params}"

    def scrum_board_url(self):
        return f"{self.host}{self.scrum_board_params}"

    def logout_url(self):
        return f"{self.host}{self.logout_params}"


class LoginPageLocators:
    login_url = UrlManager().login_url()
    login_params = UrlManager().login_params

    # First time login setup page
    continue_button = (By.ID, 'next')
    avatar_page_next_button = (By.CSS_SELECTOR, "input[value='Next']")
    explore_current_projects = (By.CSS_SELECTOR, "a[data-step-key='browseprojects']")
    login_field = (By.ID, 'login-form-username')
    password_field = (By.ID, 'login-form-password')
    login_submit_button = (By.ID, 'login-form-submit')
    system_dashboard = (By.ID, "dashboard")
    footer = (By.ID, 'footer-build-information')


class LogoutLocators:
    logout_url = UrlManager().logout_url()
    logout_submit_button = (By.ID, "confirm-logout-submit")
    login_button_link = (By.CLASS_NAME, "login-link")


class DashboardLocators:
    dashboard_url = UrlManager().dashboard_url()
    dashboard_params = UrlManager().dashboard_params
    dashboard_window = (By.CLASS_NAME, "page-type-dashboard")


class IssueLocators:
    issue_title = (By.ID, "summary-val")

    create_issue_button = (By.ID, "create_link")
    # Issue create modal form
    issue_modal = (By.ID, "create-issue-dialog")
    issue_summary_field = (By.ID, "summary")
    issue_description_field_RTE = (By.XPATH, "//div[textarea[@id='description']]//iframe")
    issue_description_field = (By.XPATH, "//textarea[@id='description']")
    tinymce_description_field = (By.ID, "tinymce")
    issue_assign_to_me_link = (By.ID, 'assign-to-me-trigger')
    issue_resolution_field = (By.ID, 'resolution')
    issue_type_field = (By.ID, 'issuetype-field')
    issue_types_options = (By.ID, "issuetype-options")
    issue_type_dropdown_elements = (By.CLASS_NAME, "aui-list-item")
    issue_ready_to_save_spinner = (By.CSS_SELECTOR, ".buttons>.throbber")
    issue_submit_button = (By.ID, "create-issue-submit")

    # Edit Issue page
    edit_issue_page = (By.ID, "issue-edit")
    edit_issue_description = (By.ID, 'description')
    edit_issue_submit = (By.ID, 'issue-edit-submit')

    # Edit Comments page
    edit_comment_add_comment_button = (By.ID, "comment-add-submit")
    edit_comment_text_field_RTE = (By.XPATH, "//div[textarea[@id='comment']]//iframe")
    edit_comment_text_field = (By.XPATH, "//textarea[@id='comment']")


class ProjectLocators:
    project_summary_property_column = (By.CLASS_NAME, 'project-meta-column')

    # projects list locators
    projects_list = (By.CSS_SELECTOR, "tbody.projects-list")
    projects_not_found = (By.CLASS_NAME, "none-panel")


class SearchLocators:
    search_issue_table = (By.ID, "issuetable")
    search_issue_content = (By.ID, "issue-content")
    search_no_issue_found = (By.CLASS_NAME, "no-results-message")


class BoardsListLocators:
    boards_list_url = UrlManager().boards_list_page_url()
    boards_list_params = UrlManager().boards_list_params

    boards_list = (By.CSS_SELECTOR, "#ghx-content-main table.aui")


class BoardLocators:
    # Scrum boards
    scrum_board_backlog_content = (By.CSS_SELECTOR, "#ghx-backlog[data-rendered]:not(.browser-metrics-stale)")
    board_columns = (By.CSS_SELECTOR, ".ghx-column")

class S3PagesLocators:
    s3_project_page = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]')
    s3_new_folder_button = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]/div/div[1]/div[1]/div[2]/button')
    s3_new_folder_input = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]/div/div[3]/table/tbody/tr[1]/td/form/div[1]/div[1]/input')
    s3_new_folder_submit = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]/div/div[3]/table/tbody/tr[1]/td/form/div[2]/button[1]')
    s3_upload_button = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]/div/div[1]/div[1]/div[1]/button')
    s3_upload_input = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]/div/div[1]/div[1]/div[1]/button/span[2]/input')
    s3_file_upload_progress_bar = (By.XPATH, '//*[@id="simplecloudfiles-project-files"]/div/div[@role=\'presentation\']')

    simplecloudfiles_menu = '//div[@class="atlaskit-portal"]/div/div[@role="menu" and starts-with(@class,"simplecloudfiles")]'
    simplecloudfiles_table = '//*[@id="simplecloudfiles-project-files"]/div//table/tbody/tr/td'

    rename_action = (By.XPATH, f'{simplecloudfiles_menu}/div/button[1]')
    delete_action = (By.XPATH, f'{simplecloudfiles_menu}/div/button[2]')

    @staticmethod
    def get_object_by_content(text):
        return By.XPATH, f'{S3PagesLocators.simplecloudfiles_table}/a/span[text() = \'{text}\']'

    @staticmethod
    def actions_button(text):
        return By.XPATH, f'{S3PagesLocators.simplecloudfiles_table}/a/span[text() = \'{text}\']/../../../td[5]/button[1]'

    @staticmethod
    def is_file_uploaded(text):
        return By.XPATH, f'{S3PagesLocators.simplecloudfiles_table}/a/span[text() = "{text}"]/../../../td[3][string-length(text()) > 0]'

    @staticmethod
    def delete_file_button(filename):
        return By.XPATH, f'{S3PagesLocators.simplecloudfiles_table}/a/span[text() = "{filename}"]/../../../td[5]/div/button[1]'

    @staticmethod
    def rename_file_input(filename):
        return By.XPATH, f'{S3PagesLocators.simplecloudfiles_table}/form//input[@value="{filename}"]'

    @staticmethod
    def rename_file_submit(filename):
        return By.XPATH, f'{S3PagesLocators.simplecloudfiles_table}/form//input[@value="{filename}"]/../../..//button[1]'